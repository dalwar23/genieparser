expected_output = {
    "Vlan211": {
        "security_level": "default",
        "ip_route_cache_flags": ["CEF", "Fast"],
        "enabled": True,
        "oper_status": "up",
        "address_determined_by": "configuration file",
        "router_discovery": False,
        "ip_multicast_fast_switching": False,
        "split_horizon": True,
        "bgp_policy_mapping": False,
        "ip_output_packet_accounting": False,
        "mtu": 1500,
        "policy_routing": False,
        "local_proxy_arp": False,
        "proxy_arp": True,
        "network_address_translation": False,
        "ip_cef_switching_turbo_vector": True,
        "icmp": {
            "redirects": "always sent",
            "mask_replies": "never sent",
            "unreachables": "always sent",
        },
        "ipv4": {
            "192.168.76.1/24": {
                "prefix_length": "24",
                "ip": "192.168.76.1",
                "secondary": False,
                "broadcast_address": "255.255.255.255",
            }
        },
        "ip_access_violation_accounting": False,
        "ip_cef_switching": True,
        "unicast_routing_topologies": {"topology": {"base": {"status": "up"}}},
        "ip_null_turbo_vector": True,
        "probe_proxy_name_replies": False,
        "ip_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "input_features": ["MCI Check"],
        "directed_broadcast_forwarding": False,
        "ip_flow_switching": False,
    },
    "GigabitEthernet0/0": {
        "security_level": "default",
        "address_determined_by": "setup command",
        "ip_route_cache_flags": ["CEF", "Fast"],
        "enabled": True,
        "oper_status": "up",
        "router_discovery": False,
        "ip_multicast_fast_switching": False,
        "split_horizon": True,
        "bgp_policy_mapping": False,
        "ip_output_packet_accounting": False,
        "mtu": 1500,
        "policy_routing": False,
        "local_proxy_arp": False,
        "vrf": "Mgmt-vrf",
        "proxy_arp": True,
        "network_address_translation": False,
        "ip_cef_switching_turbo_vector": True,
        "icmp": {
            "redirects": "always sent",
            "mask_replies": "never sent",
            "unreachables": "always sent",
        },
        "ipv4": {
            "10.1.8.134/24": {
                "prefix_length": "24",
                "ip": "10.1.8.134",
                "secondary": False,
                "broadcast_address": "255.255.255.255",
            }
        },
        "ip_access_violation_accounting": False,
        "ip_cef_switching": True,
        "unicast_routing_topologies": {"topology": {"base": {"status": "up"}}},
        "ip_null_turbo_vector": True,
        "probe_proxy_name_replies": False,
        "ip_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "input_features": ["MCI Check"],
        "directed_broadcast_forwarding": False,
        "ip_flow_switching": False,
    },
    "GigabitEthernet2": {"enabled": False, "oper_status": "down"},
    "GigabitEthernet1/0/1": {
        "security_level": "default",
        "address_determined_by": "setup command",
        "ip_route_cache_flags": ["CEF", "Fast"],
        "enabled": False,
        "oper_status": "down",
        "router_discovery": False,
        "ip_multicast_fast_switching": False,
        "split_horizon": True,
        "bgp_policy_mapping": False,
        "ip_output_packet_accounting": False,
        "mtu": 1500,
        "policy_routing": False,
        "local_proxy_arp": False,
        "proxy_arp": True,
        "network_address_translation": False,
        "ip_cef_switching_turbo_vector": True,
        "icmp": {
            "redirects": "always sent",
            "mask_replies": "never sent",
            "unreachables": "always sent",
        },
        "ipv4": {
            "10.1.1.1/24": {
                "prefix_length": "24",
                "ip": "10.1.1.1",
                "secondary": False,
                "broadcast_address": "255.255.255.255",
            },
            "10.2.2.2/24": {"prefix_length": "24", "ip": "10.2.2.2", "secondary": True},
        },
        "ip_access_violation_accounting": False,
        "ip_cef_switching": True,
        "unicast_routing_topologies": {"topology": {"base": {"status": "up"}}},
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False,
        },
        "ip_null_turbo_vector": True,
        "probe_proxy_name_replies": False,
        "ip_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "directed_broadcast_forwarding": False,
        "ip_flow_switching": False,
        "input_features": ["MCI Check", "QoS Classification", "QoS Marking"],
    },
}
