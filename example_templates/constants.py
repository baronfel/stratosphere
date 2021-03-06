ENV = {
    "dev": {
        "cidr": "10.128.0.0/14",
        "subnetworks": [
            {
                "region": "us-central1",
                "cidr": "10.128.0.0/20"
            },
            {
                "region": "us-west1",
                "cidr": "10.128.32.0/20"
            },
            {
                "region": "us-east1",
                "cidr": "10.128.64.0/20"
            },
            {
                "region": "europe-west1",
                "cidr": "10.128.96.0/20"
            },
            {
                "region": "asia-east1",
                "cidr": "10.128.128.0/20"
            }
        ],
        'gke_clusters': [
            {
                'name': 'my-cluster',
                'node_count': 1,
                'machine_type': 'n1-standard-1',
                'disk_size': 100,
                'subnetwork': 'us-central1',
                'zone': 'us-central1-b',  #  Primary zone
                'locations': ['us-central1-a', 'us-central1-b', 'us-central1-c']  #  Additional zones
            }
        ]
    },
    "prod": {
        "cidr": "10.136.0.0/14",
        "subnetworks": [
            {
                "region": "us-central1",
                "cidr": "10.136.0.0/20"
            },
            {
                "region": "us-west1",
                "cidr": "10.136.32.0/20"
            },
            {
                "region": "us-east1",
                "cidr": "10.136.64.0/20"
            },
            {
                "region": "europe-west1",
                "cidr": "10.136.96.0/20"
            },
            {
                "region": "asia-east1",
                "cidr": "10.136.128.0/20"
            }
        ]
    }
}
