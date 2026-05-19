from flask import Flask, render_template, request

app = Flask(__name__)

EMAIL_HEADERS = """
Delivered-To: billybob@gmail.com
Received: by 2002:a17:906:7945:b0:bbe:a079:78a0 with SMTP id l5csp17864ejo;
        Fri, 8 May 2026 03:45:11 -0700 (PDT)
Return-Path: <trustcompanygroup@rnicrosoft.com>
Received-SPF: fail (google.com: domain of trustcompanygroup@rnicrosoft.com
        does not designate 209.85.220.41 as permitted sender)
        client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
        dkim=fail header.i=@rnicrosoft.com;
        spf=fail (google.com: domain of trustcompanygroup@rnicrosoft.com
        does not designate 209.85.220.41 as permitted sender)
        smtp.mailfrom=trustcompanygroup@rnicrosoft.com;
        dmarc=fail (p=NONE sp=QUARANTINE dis=NONE) header.from=rnicrosoft.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=rnicrosoft.com;
        s=default; t=1778237111; x=1778841911;
        b=INVALIDBASE64STRING==
X-Received: by 2002:a05:7300:3207:b0:2c5:60d0:701e with SMTP id
        5a478bee46e88-2f85bb73083mr1095060eec.3.1778237110418;
        Fri, 08 May 2026 03:45:10 -0700 (PDT)
MIME-Version: 1.0
From: Microsoft Security Team <trustcompanygroup@rnicrosoft.com>
Date: Fri, 8 May 2026 03:44:55 -0700
Message-ID: <CAODc4WOe-dGY0twFWPqGXs-u0fWmnDfCCUXUCz8votW4wBixRA@rnicrosoft.com>
Subject: Urgent: Verify Your Microsoft Account
To: billybob@gmail.com
Content-Type: multipart/alternative; boundary="0000000000004b03d106514c178b"
"""

CORRECT_ANSWERS = {
    "spf": "fail",
    "return_path": "rnicrosoft.com",
    "dkim": "fail"
}

@app.route('/')
def index():
    return render_template('challenge.html', headers=EMAIL_HEADERS)

@app.route('/submit', methods=['POST'])
def submit():
    spf = request.form.get('spf', '').strip().lower()
    return_path = request.form.get('return_path', '').strip().lower()
    dkim = request.form.get('dkim', '').strip().lower()

    results = {
        "spf": spf == CORRECT_ANSWERS["spf"],
        "return_path": return_path == CORRECT_ANSWERS["return_path"],
        "dkim": dkim == CORRECT_ANSWERS["dkim"]
    }

    user_answers = {
        "spf": spf,
        "return_path": return_path,
        "dkim": dkim
    }

    return render_template('result.html',
                           results=results,
                           user_answers=user_answers,
                           correct=CORRECT_ANSWERS,
                           headers=EMAIL_HEADERS)

if __name__ == '__main__':
    app.run(debug=True)
