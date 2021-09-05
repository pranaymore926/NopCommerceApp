@ECHO OFF
ECHO pytest --capture=tee-sys -v -m "sanity"   --html=Reports\report.html testCases --browser chrome
rem pytest --capture=tee-sys -v -m "sanity or regression"   --html=Reports\report.html testCases --browser chrome
rem pytest --capture=tee-sys -v -m "sanity and regression"   --html=Reports\report.html testCases --browser chrome
rem pytest --capture=tee-sys -v -m "regression"   --html=Reports\report.html testCases --browser chrome
PAUSE