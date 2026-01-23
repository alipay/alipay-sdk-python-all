#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RedPacketMsgVO(object):

    def __init__(self):
        self._red_packet_id = None

    @property
    def red_packet_id(self):
        return self._red_packet_id

    @red_packet_id.setter
    def red_packet_id(self, value):
        self._red_packet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.red_packet_id:
            if hasattr(self.red_packet_id, 'to_alipay_dict'):
                params['red_packet_id'] = self.red_packet_id.to_alipay_dict()
            else:
                params['red_packet_id'] = self.red_packet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RedPacketMsgVO()
        if 'red_packet_id' in d:
            o.red_packet_id = d['red_packet_id']
        return o


