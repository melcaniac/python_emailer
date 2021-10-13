#!/bin/bash
mymailservers=(mail.tor.l torinfeml31.host.local torinfeml31.host.local mail.lon.l loninfeml31.lon.l loninfeml32.lon.l mail.rdc.l rdcinfeml31.rdc.l rdcinfeml32.rdc.l mail.prod.peopleclick.com atlinfeml31.prod.peopleclick.com atlinfeml32.prod.peopleclick.com )

for i in "${mymailservers[@]}"
do
        echo ======"$i"======
        #python emailer.py -g "$i" -f eoc@peopleclick.com -t matt@peopleclick.com -s "$i"-test -d "$i"-test
done

