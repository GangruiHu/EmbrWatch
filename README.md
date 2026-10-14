# EmbrWatch



**EmbrWatch** is an autonomous long-range FPV drone with a DJI O4 air unit and YOLOv10 object detection for early detection to prevent natrual disasters.



##  Overview

EmbrWatch combines a 7-inch long-range FPV drone with a computer vision base station/ PC. It is built to maintain long flight times while running autonomously to cover large areas and identify specific issues in real time.

## How It Works

EmbrWatch operates through a system of flight control hardware, video transmission, and AI Detection:

### 1. Flight & Navigation
* **Flight Controller & ESC Stack:** The **SoloGood F405 Stack** runs Betaflight to control the 7-inch drone in different weather conditions.
* **Autonomous Navigation:** The **HGLRC M100-5883 GPS/Compass Module** will provide us with location data, allowing us to perform position hold, precise waypoint navigation, and automated Return-to-Home (RTH) in case of signal loss.
* **Control Link:** Long-range control is possible because of the **RadioMaster Pocket Controller** sending 2.4GHz signals to the **RadioMaster RP4TD-M ELRS Receiver**, providing less than 10ms latency and a high anti interference range.

### 2. Location and Video Capture
* **Digital Transmission:** The **DJI O4 Air Unit Pro** captures clear 4K video perfeect for accurate image and threat detection. The low latnecy VTX, or video transmitter, allows for even more accurate usage.
* **FPV Monitoring:** My visual feed is received using **DJI Goggles N3** for manual changes(if neddeed), spot checks, and more situational awareness.

### 3. The AI Part/ Threat Detection using (YOLOv10)
* **Stream Transmission:** The video receiver passes the live stream into an OpenCV system running on the ground PC.
* **Detection Model:** Frames are evaluated using a custom **YOLOv10** object detection model trained on wildfire, smoke column, and thermal hotspot datasets.
* **Alert Triggering:** When threats exceed thresholds, the system flags the GPS coordinates and logs thermal/visual alerts for response.

---

##  System Specifications:

### Hardware
* Frame: 7-Inch FPV Frame
* Flight Controller & ESC Stack: Flight Controller + 4-in-1 ESC Stack
* Motors: 4x Brushless Motors
* Video Transmitter & Camera: DJI O4 Air Unit System
* Control System: ELRS Radio Receiver & RadioMaster Pocket Controller
* Propellers: 7-Inch Props
* Navigation: GPS / Compass Navigation Module
* Power & Battery: 6S 5000mAh 120C LiPo Battery & High-Gauge Battery Wires
* FPV Goggles: DJI Goggles N3

### Software & AI
* Flight Controller Software: Betaflight
* Object Detection: YOLOv10 model
* Development Environment: Python, OpenCV

## 🛠️ Project Bill of Materials (BOM)

| Category | Component | Price | Link |
| :--- | :--- | :---: | :--- |
| **Frame** | 7-Inch FPV Frame | $38 | [Amazon Link](https://www.amazon.com/gp/product/B083DVQL6K/ref=ox_sc_act_title_1?smid=A3J255IWI9K08U&psc=1) |
| **Flight Stack** | Flight Controller + 4-in-1 ESC | $82 | [Amazon Link](https://www.amazon.com/gp/product/B0CWNPZZXV/ref=ox_sc_act_title_6?smid=A1JGQIWP459RKC&psc=1) |
| **Motors** | 4x Brushless Motors | $57 | [Amazon Link](https://www.amazon.com/gp/product/B0G3F4WSP7/ref=ox_sc_act_title_5?smid=A23QGDW0H5Q266&psc=1) |
| **Digital VTx / Camera** | HD Air Unit System (DJI O4 / Caddx) | $229 | [B&H Link](https://www.bhphotovideo.com/c/product/1870780-REG/dji_cp_fp_00000233_01_o4_air_unit_pro.html) |
| **Control Receiver** | Radio Receiver | $33 | [Amazon Link](https://www.amazon.com/gp/product/B0FGJH6TSB/ref=ox_sc_act_title_4?smid=A2405ZM6GWFPMW&psc=1) |
| **Propellers** | 7-Inch Props (3–4 sets) | $15 | [Amazon Link](https://www.amazon.com/gp/product/B0C9344Q3Y/ref=ox_sc_act_title_4?smid=A17GICQ8X7LW23&psc=1) |
| **GPS / Compass** | Navigation Module | $21 | [Amazon Link](https://www.amazon.com/gp/product/B0CB5N8RQ8/ref=ox_sc_act_title_3?smid=A399B0GHKF2YQX&psc=1) |
| **Battery Wires** | Battery Wires | $10 | [Amazon Link](https://www.amazon.com/gp/product/B07QH249CR/ref=ox_sc_act_title_8?smid=A1JTH8JAMM4IYJ&psc=1) |
| **Goggles** | DJI Goggles N3 | $229 | [B&H Link](https://www.bhphotovideo.com/c/product/1975693-REG/dji_cp_rc_00000033_01_goggles_n3_us.html) |
| **Controller** | RadioMaster Pocket Transmitter | $80 | [Amazon Link](https://www.amazon.com/sspa/click?ie=UTF8&spc=MTo2NDAwNDIxNjMyNDY0MzM4OjE3OTE3NjQxMTM6c3BfYXRmOjMwMTM0NDYwMzEwMTYwMjo6MDo6&url=%2FRadiomaster-Pocket-ELRS-Transmitter-Portable%2Fdp%2FB0GWPZ96C5%2Fref%3Dsr_1_1_sspa%3Fcrid%3D2OMWDTQK2R4YX%26dib%3DeyJ2IjoiMSJ9.2JUlG1X7LrE6aPDYkvozqQo9CjO0sjmAQVzpOajtiIyoGqen9AFIZJQh_67ENvTJ9PdT0wHi1Qk-W_cjhQA4xhzVPcdaPfaft3wKuAw97z-lbhIvtmrKXn81K0bJTLRaUKXt3aNIUdwr3xZZBtqTutMDdHFRZVY5GAv60616s7HGUVEkGttVHIVonxz2SZWAm5RhM-xA19kpAAwfAIyX8o4MUC7PtwZudqItHc8qM8uH20W8S8yxPkvPI1O8f0PujCpchDcl3YOhhksTr37p3wndMDtDPhVoWPSgpua-lMY.WduESkMifzUVtHvHXlH6tPca7LFiJatBf8URlhChMHw%26dib_tag%3Dse%26keywords%3Dradio%2Bmaster%2Bpocket%26qid%3D1791764113%26refinements%3Dp_36%253A-8000%26rnid%3D386442011%26sprefix%3Dradio%2Bmaster%2Bpocke%252Caps%252C161%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1) |
| **6S Battery** | 6S 5000mAh 120C LiPo | $106 | [Amazon Link](https://www.amazon.com/gp/product/B0DNLW4W8H/ref=ox_sc_act_title_9?smid=A1KODDOPEPALCP&psc=1) |
| **Connectors** | XT90 Connector | $10 | [Amazon Link](https://www.amazon.com/Female-Bullet-Connector-RC-Battery/dp/B07C8LJMFP/ref=sr_1_9?crid=5VBCGY481O9H&dib=eyJ2IjoiMSJ9.fwhNOpMSHP2G7s4XQ6S4WUutXK9eDNvuPuZo92FtX8ATeiu3ZF5u9lg_ZXd7DVqXIxgrjPd0Qvyb-wryJWsi35plomOz_NT7QS_1HREOs1PL3f10FvluqwrNFSWSCJULBjTlxH-A0csMfTkKw2HQGA8Mx1k5Hokzj49zIsvGayaOWUpKRth9nUAAnPlW5K9b3kRW_S2Bp0Tbhqwoeb2GC0pRvJg3Ns-kF0ARvP6fkdJfKB45kFy-Y-H7h0xYzbfdczcFVyjcvYLvNw152wto1WecCT0eycpMcn4F_fpANr0.KEdWRVGT5HYenqNyJ88aKBURgtHBHBPSYURljz_vDNA&dib_tag=se&keywords=xt90+connector&qid=1791763614&sprefix=%2Caps%2C129&sr=8-9) |
| **Antenna** | SMA RHCP Antenna | $80 | [Amazon Link](https://www.amazon.com/HGLRC-Range-Antenna-Hammer-2-5dBi/dp/B08TTBFYMK/ref=sr_1_5?crid=5J8I11CQ7IDU&dib=eyJ2IjoiMSJ9.Kn5-ec6EJ8A4I5nIqUPs2FhOcJjTXY28ih2R8onuQxlumcqWoStGqo6DezMy2HH0Szy-3l4Di3RRI-oB2FlrVABwRb21J5SHx0G_L_KLwQcPPZHKgLqxmTj0CxfrO8ykZDKzti42w-oL_WPQIQvA46Auv29KFQ-AAnnL3HzsMZX2Sb08NerQ65Oj3YQqU1anktIe1PcqXgdKporjSDqFPAlBgRk9XZ5HoBVbibqDawNgZ0q5IMHQr-tZdztUcsr4PB_31tT2mWbYm6oMtFNTFmOcZd6ssfh8ETQ7-LK05qw.1YVATsguLZIXjMw1blTJCz1-Km-_ahV1xaoNSzlw5Yg&dib_tag=se&keywords=sma+rhcp+antenna&qid=1791764194&sprefix=sma+rchp+a%2Caps%2C153&sr=8-5) |
| **Adapter** | UFL to SMA Pigtail | $18 | [Amazon Link](https://www.amazon.com/Coaxial-Pigtail-Antenna-Bulkhead-Extender/dp/B098QH631G/ref=sr_1_4?crid=3PJW6NE56EBMR&dib=eyJ2IjoiMSJ9.CWSlm-Ov96tzliO_HLpP6PXalKoSCt_YqO5zV3MseFFMBgnocPsPLFi679dPTFucrO1nqP9X2uF4ddrXcOjVU54BJaIW-Tdoai0O1BUJKk34GaytmLh46Mu3gkUsz9KOOJ0RCGW_lE3iGeihErba34XNOvwIa0MEYsaRlS_ADl6MoaVBDDPGnt_Ye6SQQGQ9gd34V1UsxIhWQ1B5HLkoFb5Ey69lZ5ApOeaNKvJEu0Q.GNPL8t_NrZR1pBH1-zasfgeN7kD7ATIu00Zqlb0_Rwg&dib_tag=se&keywords=UFL+to+sma&qid=1791764270&sprefix=ufl+to+sm%2Caps%2C165&sr=8-4) |
| **Accessory** | SMA 50 Ohm Terminator | $8 | [Amazon Link](https://www.amazon.com/DHT-Electronics-coaxial-connector-Termination/dp/B00BXUYDMM/ref=sr_1_3?crid=2LGLKEK9QPC49&dib=eyJ2IjoiMSJ9.tIxrGsJVWIh80d9ZmqcbDqaSYuq3bm7liCNgi-4eeMZaVDgGOeT6uDCeZ7UaJtPgpMlDAarOiKcrgFz6zWROD6vg2vhhdOznG-xgLu0uLo6OfCtc8HjzzXg5r8QJ6F1tqb-dD99q7ca-b8nz5qbGkb9Z9SfJGhm8yJxO1vuzIWt6MhS02gEENizOnOHXDLEPiPiDiFDMTQy1H6ao1B7j5aoaIAgnnU6fvoT2CT44XDo.l-0_RUhipoibwqi3ZQRvz9vyQ1ZDWSCEoQi_9om_0PY&dib_tag=se&keywords=sma+50ohm+dummy+load&qid=1791764318&sprefix=sma+50ohm%2Caps%2C156&sr=8-3) |
| **Charger** | 18650 Battery Charger | $6 | [Amazon Link](https://www.amazon.com/Charger-Rechargeable-Battery-Lithium-Batteries/dp/B08XQSSRZK/ref=sr_1_15?crid=1S5BKM6STYO3A&dib=eyJ2IjoiMSJ9.sok3OEaF-62Zyf7S3l__3FAsxnc_EmZvG_tSLVKeWK2s0Wg-aHfFsBtrB-tO91tKzSVPdbvOug3MmF5lDgAKYrS3lcxtvUN5uJB68hahzgly57c0rtSGLcGBW3ffRoDxcUgsU2166_vEB-ZyVfdsHXmCoE3XPoCgu1Rgyp-4-hzlFULKODpTGqt_D1b_MVhIZwJsvC-T3BYp1vcJdSlBszzQ43Hu96LRq2oPZCmU0uA.I9wr1t_fg1bIlJamF0LZBscSWCk7bIRadOvCgluSBUA&dib_tag=se&keywords=18650+charger&qid=1791764370&sprefix=18650+charge%2Caps%2C167&sr=8-15) |
| **Adapter** | SMA to RP-SMA Adapter | $10 | [Amazon Link](https://www.amazon.com/BOOBRIE-Antennas-Connector-Converter-Security/dp/B0969V4QBV/ref=sr_1_6?crid=AHRF1H5UM90I&dib=eyJ2IjoiMSJ9.8A72yK3UscAK3jpd7v9pf1Yu3MKH8l26Z8CwMdxVJ90284f3E1ifcpKenCgxwdAtNWOtG3oJNNlEysZ830t9f9MFgcM_020UC6U39ajuZt24ScuRdnTapQa597Gzk5aVV8auXYffEFbCfo5Eiomgtr4-s3kQFqx_6qjnQlm7W03pnhdKk-YAewcJuNe33WcNxB23Sk7CGkAKhJ73FVVnnzvZMH4_-f7AgpoECkO4JG8.DG2UN0wsiMlpl95KbBwsVHLbvoRY35t0tviS-Q5aXLc&dib_tag=se&keywords=sma+to+rpsma&qid=1791764508&sprefix=sma+to+rpsm%2Caps%2C160&sr=8-6) |
| **Total** | | **$1,088** | |

<img width="960" height="720" alt="image" src="https://github.com/user-attachments/assets/86f80673-cae7-4e7e-91cb-e9662facb7a7" />
<img width="3428" height="1365" alt="Drone" src="https://github.com/user-attachments/assets/409dc1e4-f51d-4480-b8c2-16c4fbcc2fb4" />
<img width="605" height="507" alt="image" src="https://github.com/user-attachments/assets/889ce9f6-b20d-454f-a215-d8860cc1cca1" />


