#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupMsgDetailVO import GroupMsgDetailVO
from alipay.aop.api.domain.GroupMsgSendRecordVO import GroupMsgSendRecordVO


class GroupMsgSendDetailVO(object):

    def __init__(self):
        self._msg_detail = None
        self._send_record_list = None

    @property
    def msg_detail(self):
        return self._msg_detail

    @msg_detail.setter
    def msg_detail(self, value):
        if isinstance(value, GroupMsgDetailVO):
            self._msg_detail = value
        else:
            self._msg_detail = GroupMsgDetailVO.from_alipay_dict(value)
    @property
    def send_record_list(self):
        return self._send_record_list

    @send_record_list.setter
    def send_record_list(self, value):
        if isinstance(value, list):
            self._send_record_list = list()
            for i in value:
                if isinstance(i, GroupMsgSendRecordVO):
                    self._send_record_list.append(i)
                else:
                    self._send_record_list.append(GroupMsgSendRecordVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.msg_detail:
            if hasattr(self.msg_detail, 'to_alipay_dict'):
                params['msg_detail'] = self.msg_detail.to_alipay_dict()
            else:
                params['msg_detail'] = self.msg_detail
        if self.send_record_list:
            if isinstance(self.send_record_list, list):
                for i in range(0, len(self.send_record_list)):
                    element = self.send_record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.send_record_list[i] = element.to_alipay_dict()
            if hasattr(self.send_record_list, 'to_alipay_dict'):
                params['send_record_list'] = self.send_record_list.to_alipay_dict()
            else:
                params['send_record_list'] = self.send_record_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMsgSendDetailVO()
        if 'msg_detail' in d:
            o.msg_detail = d['msg_detail']
        if 'send_record_list' in d:
            o.send_record_list = d['send_record_list']
        return o


