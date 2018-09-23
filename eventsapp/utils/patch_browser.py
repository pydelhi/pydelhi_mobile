from kivy.utils import platform

import webbrowser
webbrowser._opened = False

if platform == 'android':
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    activity = autoclass('org.kivy.android.PythonActivity').mActivity

    @run_on_ui_thread
    def initiate_webview():
        webview = WebView(activity)
        webbrowser._webview = webview
        webbrowser._view_cached = activity.getCurrentFocus()
        settings = webbrowser._webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setUseWideViewPort(True)  # enables viewport html meta tags
        settings.setLoadWithOverviewMode(True)  # uses viewport
        settings.setSupportZoom(True)  # enables zoom
        settings.setBuiltInZoomControls(True)  # enables zoom controls
        wvc = WebViewClient()
        webbrowser._webview.setWebViewClient(wvc)

    initiate_webview()

    def _webopen(*args, **kwargs):
        #print '9'*90
        @run_on_ui_thread
        def webopen(*args, **kwargs):
            # open webview here
            url = args[0]
            webview = webbrowser._webview
            webview.resumeTimers()
            webview.clearHistory()
            webview.loadUrl("about:blank")
            webview.clearCache(True)
            webview.freeMemory()
            activity.setContentView(webview)
            webbrowser._webview.loadUrl('{}'.format(url))
            webbrowser._opened = True

        webopen(*args, **kwargs)
        return True

    @run_on_ui_thread
    def close(*args):
        if not webbrowser._webview:
            return

        wv = webbrowser._webview
        wv.clearHistory()
        wv.clearCache(True)
        wv.loadUrl("about:blank")
        wv.freeMemory()
        wv.pauseTimers()
        activity.setContentView(webbrowser._view_cached)
        webbrowser._opened = False

    webbrowser.open = _webopen
    webbrowser.close = close
