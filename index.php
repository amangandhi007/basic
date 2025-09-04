<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>K.A. Registration Form</title>
  <style>
    :root{
      --bg: #f7f7f7;
      --card: #ffffff;
      --accent: #0f172a; /* dark navy */
      --muted: #6b7280;
      --border: #e6e7e9;
      --radius: 12px;
      --gap: 20px;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }

    html,body{height:100%;}
    body{
      margin:0;
      background:linear-gradient(180deg, #ffffff 0%, var(--bg) 100%);
      display:flex;
      align-items:flex-start;
      justify-content:center;
      padding:40px 20px;
      color:var(--accent);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }

    .container{
      width:100%;
      max-width:700px;
    }

    .card{
      background:var(--card);
      border-radius:var(--radius);
      padding:36px 40px;
      box-shadow:0 6px 20px rgba(16,24,40,0.06);
      border:1px solid var(--border);
    }

    h1{
      margin:0 0 18px 0;
      font-size:34px;
      letter-spacing:1px;
      text-align:center;
      font-weight:700;
    }

    form{
      margin-top:10px;
      display:grid;
      gap:var(--gap);
    }

    .field{
      display:flex;
      flex-direction:column;
      gap:8px;
    }

    label{
      font-size:20px;
      font-weight:600;
    }

    input[type="text"], input[type="file"]{
      height:56px;
      padding:14px 16px;
      border-radius:10px;
      border:1.5px solid var(--border);
      font-size:16px;
      outline:none;
      background:#fff;
      transition:box-shadow .12s, border-color .12s;
    }

    input[type="text"]:focus{
      border-color:#c7d2fe;
      box-shadow:0 0 0 4px rgba(99,102,241,0.08);
    }

    /* Gender row */
    .gender-row{
      display:flex;
      align-items:center;
      gap:28px;
      padding-top:6px;
    }

    .radio {
      display:flex;
      align-items:center;
      gap:8px;
      font-size:18px;
      color:var(--accent);
    }

    input[type=radio]{
      width:18px;
      height:18px;
    }

    /* Profile photo area */
    .photo-area{
      border:1.5px dashed var(--border);
      border-radius:12px;
      padding:22px;
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:160px;
      background:#fff;
      position:relative;
    }

    .photo-placeholder{
      display:flex;
      flex-direction:column;
      align-items:center;
      gap:10px;
      color:var(--muted);
      font-weight:600;
    }

    .photo-preview{
      position:absolute;
      inset:14px;
      display:flex;
      align-items:center;
      justify-content:center;
    }

    .photo-preview img{
      max-width:100%;
      max-height:100%;
      object-fit:cover;
      border-radius:8px;
    }

    .small-muted{
      font-size:14px;
      color:var(--muted);
      font-weight:500;
    }

    /* Buttons */
    .btn-row{
      display:flex;
      justify-content:flex-end;
      gap:12px;
      margin-top:6px;
    }

    button{
      padding:12px 18px;
      border-radius:10px;
      border:0;
      cursor:pointer;
      font-weight:700;
      font-size:15px;
    }

    .btn-submit{
      background:#0f172a;
      color:#fff;
      box-shadow:0 6px 18px rgba(15,23,42,0.12);
    }

    .btn-reset{
      background:transparent;
      color:var(--accent);
      border:1px solid var(--border);
    }

    /* Responsive */
    @media (max-width:520px){
      .card{padding:24px}
      h1{font-size:26px}
      label{font-size:18px}
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="card" role="region" aria-label="K.A. Registration form">
      <h1>K.A. REGISTRATION FORM</h1>

      <form id="regForm"  action="insert.php" method="post" enctype="multipart/form-data">
        <div class="field">
          <label for="name">Name</label>
          <input id="name" name="name" type="text" placeholder="Enter full name" required />
        </div>

        <div class="field">
          <label for="father">Father Name</label>
          <input id="father" name="fathername" type="text" placeholder="Enter fathername" required />
        </div>

        <div class="field">
          <label>Gender</label>
          <div class="gender-row" role="radiogroup" aria-label="Gender">
            <label class="radio"><input type="radio" name="gender" value="male" required> Male</label>
            <label class="radio"><input type="radio" name="gender" value="female"> Female</label>
            <label class="radio"><input type="radio" name="gender" value="other"> Other</label>
          </div>
        </div>

        <div class="field">
          <label for="photo">Profile Photo</label>

          <div class="photo-area" id="photoArea">
            <div class="photo-placeholder" id="photoPlaceholder">
              <input type = "file" name = "image" accpect = "image/*">
              <div>Upload Photo</div>
              <div class="small-muted">PNG, JPG — max 2MB</div>
            </div>
            </div>
            </div>
        <div class="btn-row">
          <button type="reset" class="btn-reset">Reset</button>
          <button type="submit" class="btn-submit">Submit</button>
        </div>
      </form>
    </div>
  </div>

</body>
</html>