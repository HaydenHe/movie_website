import media
import fresh_tomatoes

wrestling_dad = media.Movie('Wrestling Dad!', 'https://img3.doubanio.com/view/photo/l/public/p2457983084.webp', 'http://v.youku.com/v_show/id_XMjcyNDg0ODE1Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1')
secret_superstar = media.Movie('Secret Superstar', 'https://img3.doubanio.com/view/photo/l/public/p2508925590.webp', 'http://v.youku.com/v_show/id_XMjk0NTI1MzM2NA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1')
three_idiots = media.Movie('Three Idiots', 'https://img3.doubanio.com/view/photo/l/public/p579729551.webp', 'http://v.youku.com/v_show/id_XMzIzMzQ3MTI4.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2&f=6307948')
movies = [wrestling_dad, secret_superstar, three_idiots]

fresh_tomatoes.open_movies_page(movies)

