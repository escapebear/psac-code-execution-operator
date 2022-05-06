#!/usr/bin/env python
from kubernetes import client, config, watch


def main():
    config.load_incluster_config()
    crds = client.CustomObjectsApi()

    stream = watch.Watch().stream(crds.list_cluster_custom_object, 'operators.psac.inf.elte.hu', 'v1', 'codeexecutions', resource_version='')
    for event in stream:
       print(event)


if __name__ == '__main__':
    main()