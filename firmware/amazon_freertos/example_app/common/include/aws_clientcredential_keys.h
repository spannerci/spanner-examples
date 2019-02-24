/*
 * Amazon FreeRTOS V1.4.1
 * Copyright (C) 2017 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 * http://aws.amazon.com/freertos
 * http://www.FreeRTOS.org
 */

#ifndef AWS_CLIENT_CREDENTIAL_KEYS_H
#define AWS_CLIENT_CREDENTIAL_KEYS_H

#include <stdint.h>

/*
 * PEM-encoded client certificate
 *
 * Must include the PEM header and footer:
 * "-----BEGIN CERTIFICATE-----\n"\
 * "...base64 data...\n"\
 * "-----END CERTIFICATE-----\n"
 */
#define keyCLIENT_CERTIFICATE_PEM \
"-----BEGIN CERTIFICATE-----\n"\
"MIIDWTCCAkGgAwIBAgIUGdpbxGUksGwG7nGt5i1nLhz//+8wDQYJKoZIhvcNAQEL\n"\
"BQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g\n"\
"SW5jLiBMPVNlYXR0bGUgU1Q9V2FzaGluZ3RvbiBDPVVTMB4XDTE5MDIxMzExMTkz\n"\
"NloXDTQ5MTIzMTIzNTk1OVowHjEcMBoGA1UEAwwTQVdTIElvVCBDZXJ0aWZpY2F0\n"\
"ZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKnhsrpPTJBWVRGZ27TS\n"\
"uDrHmb9IsRWnOM14DtC4ecSSXVEozCCl1YpmUms+ZSBjdAeOfCsONJcn8eqikxoM\n"\
"VSDe6kMnzAG+flIlpaXrUqX5Aed9/I1gosm4dDsWppKzIQXZN/ihnTvYM6FxanbE\n"\
"faRucBy4xMcumMyCThqrEwj/vbe3cZjVNzj3JvaWOtHcDAIdlg/mF4+pPrKhZnHt\n"\
"GcygHahsvjyONdFS9TZuGXKVQr/VDxX6jauURxg393Yv9v7xS6CRx7Ki1plPADmk\n"\
"h/ZBdjqYRPaGnvcvJf0lRwqeLK4RTEWAPLh02Jj5dnxRQBIQlcTviZ3bpwlaVz1y\n"\
"xLsCAwEAAaNgMF4wHwYDVR0jBBgwFoAU6ibL//+F2DPU7coC/BZEoLJE/3AwHQYD\n"\
"VR0OBBYEFLA7/KWTw93cIirWU18K0jSSAsBbMAwGA1UdEwEB/wQCMAAwDgYDVR0P\n"\
"AQH/BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IBAQCT3YUp85nkB02JTZLBpYt5ecRa\n"\
"DxipoqAG/UfOl8zo2jA9sROz/xclXsxknW/nZoepufL7PEjZkQ3pFV7TDrrsXLlK\n"\
"shJ160Ju6s3HTmywXdwiIjRwD9g+ZHn65EHAqTZSbIdVm289qLhDRxjCye9XBCCt\n"\
"3wd+LdfJu1IGzEyQZVPN0D7tVoAcft33BDexp7logQf0Iq91Z1MsosNPZs+xKT9V\n"\
"IrMbYkaEehVR6ksaOTlnmDS6kolwRIP1GT7mRO3/pH9dVs+8UerBJas4szA4mji9\n"\
"thFgoDkS2X8hbsS2oiYsIl6LPKJYVD78fvmIGvEVuErGicCst28SSbHZokhR\n"\
"-----END CERTIFICATE-----\n"

/*
 * PEM-encoded issuer certificate for AWS IoT Just In Time Registration (JITR).
 * This is required if you're using JITR, since the issuer (Certificate 
 * Authority) of the client certificate is used by the server for routing the 
 * device's initial request. (The device client certificate must always be 
 * sent as well.) For more information about JITR, see:
 *  https://docs.aws.amazon.com/iot/latest/developerguide/jit-provisioning.html, 
 *  https://aws.amazon.com/blogs/iot/just-in-time-registration-of-device-certificates-on-aws-iot/.
 *
 * If you're not using JITR, set below to NULL.
 * 
 * Must include the PEM header and footer:
 * "-----BEGIN CERTIFICATE-----\n"\
 * "...base64 data...\n"\
 * "-----END CERTIFICATE-----\n"
 */
#define keyJITR_DEVICE_CERTIFICATE_AUTHORITY_PEM  NULL

/*
 * PEM-encoded client private key.
 *
 * Must include the PEM header and footer:
 * "-----BEGIN RSA PRIVATE KEY-----\n"\
 * "...base64 data...\n"\
 * "-----END RSA PRIVATE KEY-----\n"
 */
#define keyCLIENT_PRIVATE_KEY_PEM \
"-----BEGIN RSA PRIVATE KEY-----\n"\
"MIIEowIBAAKCAQEAqeGyuk9MkFZVEZnbtNK4OseZv0ixFac4zXgO0Lh5xJJdUSjM\n"\
"IKXVimZSaz5lIGN0B458Kw40lyfx6qKTGgxVIN7qQyfMAb5+UiWlpetSpfkB5338\n"\
"jWCiybh0OxamkrMhBdk3+KGdO9gzoXFqdsR9pG5wHLjExy6YzIJOGqsTCP+9t7dx\n"\
"mNU3OPcm9pY60dwMAh2WD+YXj6k+sqFmce0ZzKAdqGy+PI410VL1Nm4ZcpVCv9UP\n"\
"FfqNq5RHGDf3di/2/vFLoJHHsqLWmU8AOaSH9kF2OphE9oae9y8l/SVHCp4srhFM\n"\
"RYA8uHTYmPl2fFFAEhCVxO+JndunCVpXPXLEuwIDAQABAoIBAQCcktO62em0Qo3H\n"\
"WipgX7LDIkJ3RdVJIsW8woHNJ6m7Xjc53UM+d/n3xFUEWQ61qlQ/vrh8qmwYQQ27\n"\
"9zljUaiIUkxRtvVVSjB9IAurf9e992Ik7T5/Q2jmSOZ/q2G9ZfHyxQDMXJBhnuP/\n"\
"UVwRuQogKlWUc0uSVUUpgJPiCnjR2fshT4I9th7w00X0ob7Ffyj8tH9RZ4/YmpkZ\n"\
"nr+lH1d3ERC+yQkw2Tq0sb9KVObkBJyReXKDkaWn5dxU2D217Qm4hsqrDBkpf7YA\n"\
"XCirhP+P/2Dyle6whSyYFTx2NWd5Y9QXZV9pffEnbV/vOG3/ydOPyI2tAveyuX9F\n"\
"BUnlFfBxAoGBANuT44RfG1awB052X6WbOZJoQJXCMBjmhI+9J/S8PysAYvIzZ047\n"\
"LST3MBKqphGSLRyyRa7k1yBq7SYwgpdNYJ8ybuzMjZhKdlOOkQgzEuH5RtjwCH3s\n"\
"V2gcgYHYTyIgryl+pVyk+g7qYzlNfKoVxPfjNSXYciMm7yLS3apAydTpAoGBAMYP\n"\
"hi7aY/Y2qf8yLS9gfc3V+Lxh8LsdpkfGVWJrNtzBChQ8lQGz1dSDXrLf2XhTKZYJ\n"\
"321KyqGb5RX3smGPwcLS4InFM1np3hlMbvkQvN+aMOXDvrf4l50F/lAh5VBmCzcz\n"\
"IMoRlckVIxCtSngItwf9GagBaCjdFbqOnSDDt1YDAoGAcwVDFyIi1gQbr7Q+Yiev\n"\
"vsuxmUFBpKmMIyd4+LBrfoETU8Ati0NgYI7DteOCXo3t56xS6EyjjC220Fx07ADy\n"\
"bjIi/RQhz/ahiR+TRXJLn+fOfvEt4ZieKMFV7ch7m2r3lorq4F7jRlDtbSTz+ryw\n"\
"kxGH061QDK3mcp121CpgD5ECgYAWxxhGcSVH3peEWs/pf+5X6sC1YYoe6tUBsiSF\n"\
"shDYKHcxRppYXMc9rnIInkfTV7UTpUUFu7E8DsK02Qyxvaep8TiTf5NdRtEdFbY5\n"\
"fJxMFt6CvhVD8Rn2nAbYTl2h9mpZyc5+jrEsM/sZYuSKk24BRDFcKfVBpdNm5hnZ\n"\
"98gw4wKBgA/xqm6Du0rIQ0CV8KjMCAAhB7RxyLHfZFAKQVrzpu54Qk0pgcAbVkCk\n"\
"HRgvT8bJFfvCx8Je8voI6q5Oolrh8n7Pbft1cmw4Fuyd3ypHxBSaLHB0Gx3eimjM\n"\
"SZ1PGyMKqeIcurPLwNn+2CO2Rips62RUs3wAkJyEya6KArfvuYw+\n"\
"-----END RSA PRIVATE KEY-----\n"

/* The constants above are set to const char * pointers defined in aws_demo_runner.c,
 * and externed here for use in C files.  NOTE!  THIS IS DONE FOR CONVENIENCE
 * DURING AN EVALUATION PHASE AND IS NOT GOOD PRACTICE FOR PRODUCTION SYSTEMS 
 * WHICH MUST STORE KEYS SECURELY. */
extern const char clientcredentialCLIENT_CERTIFICATE_PEM[];
extern const char* clientcredentialJITR_DEVICE_CERTIFICATE_AUTHORITY_PEM;
extern const char clientcredentialCLIENT_PRIVATE_KEY_PEM[];
extern const uint32_t clientcredentialCLIENT_CERTIFICATE_LENGTH;
extern const uint32_t clientcredentialCLIENT_PRIVATE_KEY_LENGTH;

#endif /* AWS_CLIENT_CREDENTIAL_KEYS_H */
