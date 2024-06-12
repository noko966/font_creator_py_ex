def get_html_template():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="styles.css" />
    <style>
      * {
        box-sizing: border-box;
      }
      html,
      body {
        margin: 0;
        padding: 0;
      }
      .icons_container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        column-gap: 24px;
        row-gap: 24px;
        padding: 16px;
        background: var(--bodyBg);
      }

      .icon_demo {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: var(--bodyBg2);
        border: 1px solid var(--bodyBg3);
        row-gap: 6px;
        border-radius: 12px;
        padding: 12px;
        transition: all 0.3s;
        cursor: pointer;
        overflow: hidden;
      }

      .card-client {
        background: #2cb5a0;
        width: 13rem;
        padding-top: 25px;
        padding-bottom: 25px;
        padding-left: 20px;
        padding-right: 20px;
        border: 4px solid #7cdacc;
        box-shadow: 0 6px 10px rgba(207, 212, 222, 1);
        border-radius: 10px;
        text-align: center;
        color: #fff;
        font-family: "Poppins", sans-serif;
        transition: all 0.3s ease;
      }

      .card-client:hover {
        transform: translateY(-10px);
      }

      .icon_main {
        overflow: hidden;
        object-fit: cover;
        width: 5rem;
        height: 5rem;
        border: 4px solid #7cdacc;
        border-radius: 999px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
      }

      .icon_main > i {
        fill: currentColor;
        --icoSize: 48px;
      }

      html {
        background: var(--bodyBg);
        color: var(--bodyTxt);
        font-family: Arial;
      }

      .icon_demo_row {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }

      .icon_demo_row_cont {
        margin-bottom: 8px;
      }

      .icon_demo_row_cont::before {
        content: "";
        display: block;
        width: 100%;
        height: 2px;
        margin: 20px 0;
        background: #7cdacc;
      }

      .btn_demo_row {
        display: flex;
        align-items: center;
        column-gap: 16px;
      }

      .btn_demo {
        width: 100%;
        position: relative;
        padding: 10px 22px;
        border-radius: 6px;
        border: none;
        color: #fff;
        cursor: pointer;
        background-color: var(--dominantBg);
        transition: all 0.2s ease;
      }

      .btn_demo:active {
        transform: scale(0.96);
      }

      .btn_demo:before,
      .btn_demo:after {
        position: absolute;
        content: "";
        width: 150%;
        left: 50%;
        height: 100%;
        transform: translateX(-50%);
        z-index: -1000;
        background-repeat: no-repeat;
      }

      .btn_demo:hover:before {
        top: -70%;
        background-image: radial-gradient(
            circle,
            var(--dominantBg) 20%,
            transparent 20%
          ),
          radial-gradient(
            circle,
            transparent 20%,
            var(--dominantBg) 20%,
            transparent 30%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(
            circle,
            transparent 10%,
            var(--dominantBg) 15%,
            transparent 20%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%);
        background-size: 10% 10%, 20% 20%, 15% 15%, 20% 20%, 18% 18%, 10% 10%,
          15% 15%, 10% 10%, 18% 18%;
        background-position: 50% 120%;
        animation: greentopBubbles 0.6s ease;
      }

      @keyframes greentopBubbles {
        0% {
          background-position: 5% 90%, 10% 90%, 10% 90%, 15% 90%, 25% 90%,
            25% 90%, 40% 90%, 55% 90%, 70% 90%;
        }

        50% {
          background-position: 0% 80%, 0% 20%, 10% 40%, 20% 0%, 30% 30%, 22% 50%,
            50% 50%, 65% 20%, 90% 30%;
        }

        100% {
          background-position: 0% 70%, 0% 10%, 10% 30%, 20% -10%, 30% 20%,
            22% 40%, 50% 40%, 65% 10%, 90% 20%;
          background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
        }
      }

      .btn_demo:active::after {
        bottom: -70%;
        background-image: radial-gradient(
            circle,
            var(--dominantBg) 20%,
            transparent 20%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(
            circle,
            transparent 10%,
            var(--dominantBg) 15%,
            transparent 20%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%);
        background-size: 15% 15%, 20% 20%, 18% 18%, 20% 20%, 15% 15%, 20% 20%,
          18% 18%;
        background-position: 50% 0%;
        animation: greenbottomBubbles 0.6s ease;
      }

      @keyframes greenbottomBubbles {
        0% {
          background-position: 10% -10%, 30% 10%, 55% -10%, 70% -10%, 85% -10%,
            70% -10%, 70% 0%;
        }

        50% {
          background-position: 0% 80%, 20% 80%, 45% 60%, 60% 100%, 75% 70%,
            95% 60%, 105% 0%;
        }

        100% {
          background-position: 0% 90%, 20% 90%, 45% 70%, 60% 110%, 75% 80%,
            95% 70%, 110% 10%;
          background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
        }
      }

      .message {
        display: none;
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: black;
        color: white;
        padding: 10px;
        border-radius: 5px;
      }
    </style>
  </head>
  <body>
    <div class="icons_container">
"""

def get_css_template(FONT_FILE_NAME, FONT_FAMILY_NAME,ICON_SIZE, CSS_CLASS ):

  
  return f"""
@font-face {{
  font-family: "{FONT_FAMILY_NAME}";
  src: url("{FONT_FILE_NAME}.eot");
  src: url("{FONT_FILE_NAME}.eot?#iefix") format("embedded-opentype"),
    url("{FONT_FILE_NAME}.woff2") format("woff2"),
    url("{FONT_FILE_NAME}.woff") format("woff"),
    url("{FONT_FILE_NAME}.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
  font-display: block;
}}

:root{{
  --bodyBg: #e8e8e8;
  --bodyBg2: #141f27;
  --bodyBg3: #445c6f;
  --bodyTxt: rgba(255,255,255,0.9);
  --bodyTxt2: rgba(255,255,255,0.6);
  --dominantBg: #0b293d;
  --dominantBg2: #14496d;
  --dominantBg3: #286a96;
  --dominantTxt: rgba(255,255,255,0.9);
  --dominantTxt2: rgba(255,255,255,0.6);
  --accentBg: #00b6ff;
  --accentBg2: #33454d;
  --accentTxt: rgba(255,255,255,0.9);
  --icoSize: {ICON_SIZE}px;
}}

.dynamic_icon {{
  font-family: "iconsDinamicMenu";
  font-size: 46px;
  line-height: 0.8;
}}

.icon_demo:hover {{
}}

.icon_demo > strong {{
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}}
.icon_demo_e {{
    background: var(--dominantBg2);
    border: 1px solid var(--dominantBg3);
    row-gap: 12px;
    border-radius: 12px; 
}}

[class^="{CSS_CLASS}"],
[class*=" {CSS_CLASS}"],
.{CSS_CLASS} {{
  font-family: "{FONT_FAMILY_NAME}";
  display: inline-block;
  flex-shrink: 0;
  width: var(--icoSize);
  height: var(--icoSize);
    font-size: calc(var(--icoSize) * 2);
  text-align: center;
  vertical-align: middle;
  font-weight: normal;
  font-style: normal;
  speak: none;
  text-decoration: inherit;
  text-transform: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  direction: ltr !important;
  content: "\\E0000";
}}

.ico_size-xs{{
    --icoSize: 16px;
}}
.ico_size-sm{{
    --icoSize: 20px;
}}
.ico_size-md{{
    --icoSize: 24px;
}}
.ico_size-lg{{
    --icoSize: 28px;
}}
.ico_size-xl{{
    --icoSize: 32px;
}}
"""
