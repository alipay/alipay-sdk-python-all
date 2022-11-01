#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsFacecheckSendModel(object):

    def __init__(self):
        self._dev_id = None
        self._face_id = None
        self._floor_num = None
        self._out_request_id = None
        self._phone_no = None
        self._project_id = None
        self._sn_list = None

    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def floor_num(self):
        return self._floor_num

    @floor_num.setter
    def floor_num(self, value):
        self._floor_num = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def sn_list(self):
        return self._sn_list

    @sn_list.setter
    def sn_list(self, value):
        if isinstance(value, list):
            self._sn_list = list()
            for i in value:
                self._sn_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.floor_num:
            if hasattr(self.floor_num, 'to_alipay_dict'):
                params['floor_num'] = self.floor_num.to_alipay_dict()
            else:
                params['floor_num'] = self.floor_num
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.sn_list:
            if isinstance(self.sn_list, list):
                for i in range(0, len(self.sn_list)):
                    element = self.sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_list[i] = element.to_alipay_dict()
            if hasattr(self.sn_list, 'to_alipay_dict'):
                params['sn_list'] = self.sn_list.to_alipay_dict()
            else:
                params['sn_list'] = self.sn_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsFacecheckSendModel()
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'floor_num' in d:
            o.floor_num = d['floor_num']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'sn_list' in d:
            o.sn_list = d['sn_list']
        return o


