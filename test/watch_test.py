#!/usr/bin/env python
from kubernetes import client, config, watch
import json


def main():
    config.load_incluster_config()
    crds = client.CustomObjectsApi()

    stream = watch.Watch().stream(crds.list_cluster_custom_object, 'operators.psac.inf.elte.hu', 'v1', 'codeexecutions', resource_version='')
    for event in stream:
        if event['raw_object']['metadata']['namespace'] == 'code-execution':
           print(json.dumps(event['raw_object']['spec'], indent=4))


if __name__ == '__main__':
    main()