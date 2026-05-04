# Site assets

Drop the official CPDSE logo files here, named exactly as below — `site/index.html`
references them by these filenames. Until they are present the page degrades to
a small "CPDSE" text fallback in the header (the `onerror` handler on the
`<img>` tag swaps it in).

| Filename                  | Where used         | Source from identity PDF       |
|---------------------------|--------------------|--------------------------------|
| `logo-wide-forest.svg`    | Header             | "Wide logo", Forest Green      |
| `logo-square-forest.svg`  | Footer             | "Square-shaped logos", Forest  |
| `logo-snake-forest.svg`   | (optional, decor)  | "Snake without text", Forest   |
| `favicon.svg`             | Browser tab        | snake mark, simplified         |

SVG is preferred. PNG also works — just rename the file to `.svg` is not
correct; instead update the `<img src="…">` extension in `site/index.html` to
match what you drop in.
