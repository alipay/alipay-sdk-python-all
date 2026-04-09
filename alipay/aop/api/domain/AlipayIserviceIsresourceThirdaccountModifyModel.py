#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceThirdaccountModifyModel(object):

    def __init__(self):
        self._ext_info = None
        self._external_acc_id = None
        self._status = None
        self._tnt_inst_id = None
        self._verify_user_id = None
        self._workstation = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def external_acc_id(self):
        return self._external_acc_id

    @external_acc_id.setter
    def external_acc_id(self, value):
        self._external_acc_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def verify_user_id(self):
        return self._verify_user_id

    @verify_user_id.setter
    def verify_user_id(self, value):
        self._verify_user_id = value
    @property
    def workstation(self):
        return self._workstation

    @workstation.setter
    def workstation(self, value):
        self._workstation = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_acc_id:
            if hasattr(self.external_acc_id, 'to_alipay_dict'):
                params['external_acc_id'] = self.external_acc_id.to_alipay_dict()
            else:
                params['external_acc_id'] = self.external_acc_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.verify_user_id:
            if hasattr(self.verify_user_id, 'to_alipay_dict'):
                params['verify_user_id'] = self.verify_user_id.to_alipay_dict()
            else:
                params['verify_user_id'] = self.verify_user_id
        if self.workstation:
            if hasattr(self.workstation, 'to_alipay_dict'):
                params['workstation'] = self.workstation.to_alipay_dict()
            else:
                params['workstation'] = self.workstation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceThirdaccountModifyModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_acc_id' in d:
            o.external_acc_id = d['external_acc_id']
        if 'status' in d:
            o.status = d['status']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'verify_user_id' in d:
            o.verify_user_id = d['verify_user_id']
        if 'workstation' in d:
            o.workstation = d['workstation']
        return o


