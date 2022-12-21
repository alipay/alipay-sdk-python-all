#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NodeOperateDTO import NodeOperateDTO


class ApproveNodePageGroupDTO(object):

    def __init__(self):
        self._ant_process_group_puid = None
        self._approve_node_group_list = None

    @property
    def ant_process_group_puid(self):
        return self._ant_process_group_puid

    @ant_process_group_puid.setter
    def ant_process_group_puid(self, value):
        self._ant_process_group_puid = value
    @property
    def approve_node_group_list(self):
        return self._approve_node_group_list

    @approve_node_group_list.setter
    def approve_node_group_list(self, value):
        if isinstance(value, list):
            self._approve_node_group_list = list()
            for i in value:
                if isinstance(i, NodeOperateDTO):
                    self._approve_node_group_list.append(i)
                else:
                    self._approve_node_group_list.append(NodeOperateDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ant_process_group_puid:
            if hasattr(self.ant_process_group_puid, 'to_alipay_dict'):
                params['ant_process_group_puid'] = self.ant_process_group_puid.to_alipay_dict()
            else:
                params['ant_process_group_puid'] = self.ant_process_group_puid
        if self.approve_node_group_list:
            if isinstance(self.approve_node_group_list, list):
                for i in range(0, len(self.approve_node_group_list)):
                    element = self.approve_node_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.approve_node_group_list[i] = element.to_alipay_dict()
            if hasattr(self.approve_node_group_list, 'to_alipay_dict'):
                params['approve_node_group_list'] = self.approve_node_group_list.to_alipay_dict()
            else:
                params['approve_node_group_list'] = self.approve_node_group_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApproveNodePageGroupDTO()
        if 'ant_process_group_puid' in d:
            o.ant_process_group_puid = d['ant_process_group_puid']
        if 'approve_node_group_list' in d:
            o.approve_node_group_list = d['approve_node_group_list']
        return o


