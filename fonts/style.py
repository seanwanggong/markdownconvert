DEFAULT_STYLE = """
@font-face {
    font-family: 'NotoSansCJK';
    src: url('fonts/方正兰亭黑简体.ttf');
}
@font-face {
  font-family: 'NotoColorEmoji';
  src: url('fonts/NotoColorEmoji-Regular.ttf');
}
@page {
    background: #fff;
    margin: 40px 0;
}
html, body {
    font-family: 'NotoColorEmoji','NotoSansCJK', Arial, sans-serif;
    background: #fff;
    color: #222;
    line-height: 1.7;
    padding: 0 48px 32px 48px;
}
h1 {
    color: #1976d2;
    font-size: 2.2em;
    font-weight: 800;
    border-bottom: 2px solid #90caf9;
    margin-top: 1em;
    margin-bottom: 0.5em;
    padding-bottom: 0.2em;
}
h2, h3 {
    color: #1976d2;
    font-size: 1.4em;
    font-weight: 700;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
}
p {
    margin: 1em 0;
    font-size: 1.08em;
}
ul, ol {
    margin: 1em 0 1em 2em;
    font-size: 1.05em;
}
blockquote {
    background: #f5f5f5;
    border-left: 4px solid #1976d2;
    margin: 1.2em 0;
    padding: 0.8em 1.2em;
    color: #1976d2;
    font-size: 1.05em;
}
code {
    background: #f5f5f5;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-size: 1em;
}
pre {
    background: #23272f;
    color: #fff;
    padding: 1em;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 1em;
    box-shadow: 0 2px 8px #0001;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.5em 0;
    font-size: 1.02em;
}
th, td {
    border: 1px solid #bbb;
    padding: 8px 12px;
    text-align: left;
}
th {
    background: #e3f2fd;
    color: #1976d2;
    font-size: 1.08em;
}
tr:nth-child(even) {
    background: #f5f5f5;
}
hr {
    border: none;
    border-top: 2px solid #90caf9;
    margin: 2em 0;
}
img {
    display: block;
    margin: 2em auto;
    max-width: 80%;
    border-radius: 6px;
    box-shadow: 0 2px 8px #0002;
}
"""

TECH_BLUE_STYLE = """
@font-face {
    font-family: 'NotoSansCJK';
    src: url('fonts/方正兰亭黑简体.ttf');
}
@font-face {
  font-family: 'NotoColorEmoji';
  src: url('fonts/NotoColorEmoji-Regular.ttf');
}
@page {
    background: #e3f2fd;
    margin: 40px 0;
}
html, body {
    font-family: 'NotoColorEmoji','NotoSansCJK', Arial, sans-serif;
    background: #e3f2fd;
    color: #1565c0;
    line-height: 1.7;
    padding: 0 48px 32px 48px;
}
h1 {
    color: #0d47a1;
    font-size: 2.4em;
    font-weight: 900;
    border-bottom: 3px solid #1976d2;
    margin-top: 1em;
    margin-bottom: 0.5em;
    padding-bottom: 0.2em;
}
h2, h3 {
    color: #1976d2;
    font-size: 1.3em;
    font-weight: 700;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
}
p {
    margin: 1em 0;
    font-size: 1.08em;
}
ul, ol {
    margin: 1em 0 1em 2em;
    font-size: 1.05em;
}
blockquote {
    background: #bbdefb;
    border-left: 5px solid #1976d2;
    margin: 1.2em 0;
    padding: 0.8em 1.2em;
    color: #0d47a1;
    font-size: 1.05em;
}
code {
    background: #e3f2fd;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-size: 1em;
}
pre {
    background: #23272f;
    color: #fff;
    padding: 1em;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 1em;
    box-shadow: 0 2px 8px #0001;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.5em 0;
    font-size: 1.02em;
}
th, td {
    border: 1px solid #90caf9;
    padding: 8px 12px;
    text-align: left;
}
th {
    background: #1976d2;
    color: #fff;
    font-size: 1.08em;
}
tr:nth-child(even) {
    background: #e3f2fd;
}
hr {
    border: none;
    border-top: 2px solid #1976d2;
    margin: 2em 0;
}
img {
    display: block;
    margin: 2em auto;
    max-width: 80%;
    border-radius: 6px;
    box-shadow: 0 2px 8px #0002;
}
"""

BUSINESS_DARK_STYLE = """
@font-face {
    font-family: 'NotoSansCJK';
    src: url('fonts/方正兰亭黑简体.ttf');
}
@font-face {
  font-family: 'NotoColorEmoji';
  src: url('fonts/NotoColorEmoji-Regular.ttf');
}
@page {
    background: #23272f;
    margin: 40px 0;
}
html, body {
    font-family: 'NotoColorEmoji','NotoSansCJK', Arial, sans-serif;
    background: #23272f;
    color: #f5f5f5;
    line-height: 1.7;
    padding: 0 48px 32px 48px;
}
h1 {
    color: #ffb300;
    font-size: 2.4em;
    font-weight: 900;
    border-bottom: 3px solid #ffb300;
    margin-top: 1em;
    margin-bottom: 0.5em;
    padding-bottom: 0.2em;
}
h2, h3 {
    color: #ffe082;
    font-size: 1.3em;
    font-weight: 700;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
}
p {
    margin: 1em 0;
    font-size: 1.08em;
}
ul, ol {
    margin: 1em 0 1em 2em;
    font-size: 1.05em;
}
blockquote {
    background: #333;
    border-left: 5px solid #ffb300;
    margin: 1.2em 0;
    padding: 0.8em 1.2em;
    color: #ffe082;
    font-size: 1.05em;
}
code {
    background: #333;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-size: 1em;
}
pre {
    background: #111;
    color: #ffe082;
    padding: 1em;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 1em;
    box-shadow: 0 2px 8px #0003;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.5em 0;
    font-size: 1.02em;
}
th, td {
    border: 1px solid #444;
    padding: 8px 12px;
    text-align: left;
}
th {
    background: #333;
    color: #ffb300;
    font-size: 1.08em;
}
tr:nth-child(even) {
    background: #2c2f36;
}
hr {
    border: none;
    border-top: 2px solid #ffb300;
    margin: 2em 0;
}
img {
    display: block;
    margin: 2em auto;
    max-width: 80%;
    border-radius: 6px;
    box-shadow: 0 2px 8px #0004;
}
"""

PASTEL_STYLE = """
@font-face {
    font-family: 'NotoSansCJK';
    src: url('fonts/方正兰亭黑简体.ttf');
}
@font-face {
  font-family: 'NotoColorEmoji';
  src: url('fonts/NotoColorEmoji-Regular.ttf');
}
@page {
    background: #fdf6f0;
    margin: 40px 0;
}
html, body {
    font-family: 'NotoColorEmoji','NotoSansCJK', Arial, sans-serif;
    background: #fdf6f0;
    color: #a47149;
    line-height: 1.7;
    padding: 0 48px 32px 48px;
}
h1 {
    color: #f48fb1;
    font-size: 2.3em;
    font-weight: 900;
    border-bottom: 3px solid #f8bbd0;
    margin-top: 1em;
    margin-bottom: 0.5em;
    padding-bottom: 0.2em;
}
h2, h3 {
    color: #f8bbd0;
    font-size: 1.3em;
    font-weight: 700;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
}
p {
    margin: 1em 0;
    font-size: 1.08em;
}
ul, ol {
    margin: 1em 0 1em 2em;
    font-size: 1.05em;
}
blockquote {
    background: #fce4ec;
    border-left: 5px solid #f8bbd0;
    margin: 1.2em 0;
    padding: 0.8em 1.2em;
    color: #a47149;
    font-size: 1.05em;
}
code {
    background: #fce4ec;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-size: 1em;
}
pre {
    background: #f8bbd0;
    color: #a47149;
    padding: 1em;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 1em;
    box-shadow: 0 2px 8px #0001;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.5em 0;
    font-size: 1.02em;
}
th, td {
    border: 1px solid #f8bbd0;
    padding: 8px 12px;
    text-align: left;
}
th {
    background: #f8bbd0;
    color: #a47149;
    font-size: 1.08em;
}
tr:nth-child(even) {
    background: #fce4ec;
}
hr {
    border: none;
    border-top: 2px solid #f8bbd0;
    margin: 2em 0;
}
img {
    display: block;
    margin: 2em auto;
    max-width: 80%;
    border-radius: 6px;
    box-shadow: 0 2px 8px #0002;
}
"""
GRAND_STYLE = """
@font-face {
    font-family: 'NotoSansCJK';
    src: url('fonts/方正兰亭黑简体.ttf');
}
@font-face {
  font-family: 'NotoColorEmoji';
  src: url('fonts/NotoColorEmoji-Regular.ttf');
}
@page {
    background: #f4f7fa;
    margin: 40px 0;
}
html, body {
    font-family: 'NotoColorEmoji','NotoSansCJK', Arial, sans-serif;
    background: #f4f7fa;
    color: #222;
    line-height: 1.8;
    padding: 0 60px 40px 60px;
}
h1 {
    color: #1a237e;
    font-size: 2.8em;
    font-weight: 900;
    letter-spacing: 2px;
    margin-top: 0.8em;
    margin-bottom: 0.5em;
    border-bottom: 4px solid #3949ab;
    padding-bottom: 0.2em;
}
h2, h3 {
    color: #3949ab;
    font-size: 1.6em;
    font-weight: 700;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}
p {
    margin: 1.2em 0;
    font-size: 1.15em;
}
ul, ol {
    margin: 1em 0 1em 2em;
    font-size: 1.1em;
}
blockquote {
    background: #e3eafc;
    border-left: 6px solid #3949ab;
    margin: 1.5em 0;
    padding: 1em 1.5em;
    color: #283593;
    font-size: 1.1em;
    font-style: italic;
}
code {
    background: #f5f5f5;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-size: 1em;
}
pre {
    background: #23272f;
    color: #fff;
    padding: 1.2em;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 1em;
    box-shadow: 0 2px 12px #0001;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 2em 0;
    font-size: 1.05em;
}
th, td {
    border: 1.5px solid #b0bec5;
    padding: 10px 16px;
    text-align: left;
}
th {
    background: #3949ab;
    color: #fff;
    font-size: 1.1em;
}
tr:nth-child(even) {
    background: #e8eaf6;
}
hr {
    border: none;
    border-top: 2px solid #90caf9;
    margin: 2em 0;
}
img {
    display: block;
    margin: 2em auto;
    max-width: 80%;
    border-radius: 8px;
    box-shadow: 0 2px 12px #0002;
}
"""