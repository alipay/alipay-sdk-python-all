#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NOrderTagActiveDataDTO(object):

    def __init__(self):
        self._coil_no = None
        self._tag_id = None
        self._touch_cnt = None
        self._touch_user_cnt = None

    @property
    def coil_no(self):
        return self._coil_no

    @coil_no.setter
    def coil_no(self, value):
        self._coil_no = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def touch_cnt(self):
        return self._touch_cnt

    @touch_cnt.setter
    def touch_cnt(self, value):
        self._touch_cnt = value
    @property
    def touch_user_cnt(self):
        return self._touch_user_cnt

    @touch_user_cnt.setter
    def touch_user_cnt(self, value):
        self._touch_user_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.coil_no:
            if hasattr(self.coil_no, 'to_alipay_dict'):
                params['coil_no'] = self.coil_no.to_alipay_dict()
            else:
                params['coil_no'] = self.coil_no
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.touch_cnt:
            if hasattr(self.touch_cnt, 'to_alipay_dict'):
                params['touch_cnt'] = self.touch_cnt.to_alipay_dict()
            else:
                params['touch_cnt'] = self.touch_cnt
        if self.touch_user_cnt:
            if hasattr(self.touch_user_cnt, 'to_alipay_dict'):
                params['touch_user_cnt'] = self.touch_user_cnt.to_alipay_dict()
            else:
                params['touch_user_cnt'] = self.touch_user_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NOrderTagActiveDataDTO()
        if 'coil_no' in d:
            o.coil_no = d['coil_no']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'touch_cnt' in d:
            o.touch_cnt = d['touch_cnt']
        if 'touch_user_cnt' in d:
            o.touch_user_cnt = d['touch_user_cnt']
        return o


