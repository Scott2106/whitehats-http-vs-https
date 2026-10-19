# HTTP vs HTTPS Login Demo

Flask login page served over HTTPS (port 5000) and HTTP (port 5001), run in Docker.


## Setup

**Requirements:** Docker Desktop (running)

### 1. Generate the certificate

```bash
pip install cryptography
python makecert.py
```

This creates `cert.pem` and `key.pem` in the project folder.

### 2. Convert the cert to `.crt`

Make a copy of `cert.pem` named `cert.crt`:

```bash
copy cert.pem cert.crt        # Windows
# cp cert.pem cert.crt        # Mac / Linux
```

### 3. Trust the cert on Windows [click here for more details ] (https://docs.google.com/document/d/1r7OCMe1qNxs2VyINuTBSqkUC-T5PqsugJTfgQyfKYKE/edit?usp=sharing)

1. Double-click `cert.crt`
2. Click **Install Certificate**
3. Select **Current User**, then **Next**
4. Select **Place all certificates in the following store**, then **Browse**
5. Choose **Trusted Root Certification Authorities**, then **OK**
6. **Next**, **Finish**, then **Yes** on the security prompt
7. Fully close and reopen Chrome

### 4. Build and run

```bash
docker compose up --build
```

### 5. Open

- HTTPS: https://localhost:5000
- HTTP: http://localhost:5001

Type the full URL with `https://`. `localhost:5000` alone defaults to HTTP and fails.

## Stop / Restart

```bash
docker compose down    # stop and remove
docker compose up      # start again (add --build after code changes)
```

## Notes

- ** Sometimes, your connection is not private(not safe) warning may show up even after u have trusted the cert. In this case, please fully close your current browser and restart. 
