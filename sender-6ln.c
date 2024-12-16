#include "contiki.h"
#include "net/netstack.h"
#include "net/ipv6/simple-udp.h"
#include <string.h>
#include <stdio.h>
#include "sys/log.h"

#define PORT_SENDER xx
#define PORT_RECV xx

/*---------------------------------------------------------------------------*/
PROCESS(udp_sender, "Sender UDP");
AUTOSTART_PROCESSES(&udp_sender);
/*---------------------------------------------------------------------------*/
PROCESS_THREAD(udp_sender, ev, data)
{
    PROCESS_BEGIN();

    PROCESS_END();
}
/*---------------------------------------------------------------------------*/
