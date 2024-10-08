#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupInstanceMsgSendDetailVO import GroupInstanceMsgSendDetailVO


class GroupMsgSendRecordVO(object):

    def __init__(self):
        self._group_id = None
        self._group_name = None
        self._send_detail_list = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def send_detail_list(self):
        return self._send_detail_list

    @send_detail_list.setter
    def send_detail_list(self, value):
        if isinstance(value, list):
            self._send_detail_list = list()
            for i in value:
                if isinstance(i, GroupInstanceMsgSendDetailVO):
                    self._send_detail_list.append(i)
                else:
                    self._send_detail_list.append(GroupInstanceMsgSendDetailVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.send_detail_list:
            if isinstance(self.send_detail_list, list):
                for i in range(0, len(self.send_detail_list)):
                    element = self.send_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.send_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.send_detail_list, 'to_alipay_dict'):
                params['send_detail_list'] = self.send_detail_list.to_alipay_dict()
            else:
                params['send_detail_list'] = self.send_detail_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMsgSendRecordVO()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'send_detail_list' in d:
            o.send_detail_list = d['send_detail_list']
        return o


