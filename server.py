"""Start a no-dependency, loopback-only local web server for the skin editor."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

if __name__ == '__main__':
    folder = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(folder))
    for port in range(5500, 5511):
        try:
            server = ThreadingHTTPServer(('127.0.0.1', port), handler)
            break
        except OSError:
            continue
    else:
        raise SystemExit('5500–5510 連接埠皆被占用，請關閉其他本機伺服器後再試。')
    url = f'http://127.0.0.1:{server.server_port}/'
    print(f'\nMinecraft Skin 樣式轉換器已啟動: {url}')
    print('請勿關閉這個視窗。完成使用後按 Ctrl+C 停止伺服器。\n')
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n伺服器已停止。')
    finally:
        server.server_close()
