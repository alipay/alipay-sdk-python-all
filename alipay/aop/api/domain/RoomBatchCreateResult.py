#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoomBatchCreateResult(object):

    def __init__(self):
        self._fail_code = None
        self._fail_msg = None
        self._out_room_id = None
        self._room_id = None

    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_msg(self):
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, value):
        self._fail_msg = value
    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.fail_msg:
            if hasattr(self.fail_msg, 'to_alipay_dict'):
                params['fail_msg'] = self.fail_msg.to_alipay_dict()
            else:
                params['fail_msg'] = self.fail_msg
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoomBatchCreateResult()
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'fail_msg' in d:
            o.fail_msg = d['fail_msg']
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'room_id' in d:
            o.room_id = d['room_id']
        return o


