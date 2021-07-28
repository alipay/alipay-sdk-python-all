#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntforestAccountTransferModel(object):

    def __init__(self):
        self._energy_account_from = None
        self._energy_account_to = None
        self._energy_count = None
        self._ext_info = None
        self._out_biz_no = None
        self._transfer_type = None
        self._user_id = None

    @property
    def energy_account_from(self):
        return self._energy_account_from

    @energy_account_from.setter
    def energy_account_from(self, value):
        self._energy_account_from = value
    @property
    def energy_account_to(self):
        return self._energy_account_to

    @energy_account_to.setter
    def energy_account_to(self, value):
        self._energy_account_to = value
    @property
    def energy_count(self):
        return self._energy_count

    @energy_count.setter
    def energy_count(self, value):
        self._energy_count = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def transfer_type(self):
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, value):
        self._transfer_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.energy_account_from:
            if hasattr(self.energy_account_from, 'to_alipay_dict'):
                params['energy_account_from'] = self.energy_account_from.to_alipay_dict()
            else:
                params['energy_account_from'] = self.energy_account_from
        if self.energy_account_to:
            if hasattr(self.energy_account_to, 'to_alipay_dict'):
                params['energy_account_to'] = self.energy_account_to.to_alipay_dict()
            else:
                params['energy_account_to'] = self.energy_account_to
        if self.energy_count:
            if hasattr(self.energy_count, 'to_alipay_dict'):
                params['energy_count'] = self.energy_count.to_alipay_dict()
            else:
                params['energy_count'] = self.energy_count
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.transfer_type:
            if hasattr(self.transfer_type, 'to_alipay_dict'):
                params['transfer_type'] = self.transfer_type.to_alipay_dict()
            else:
                params['transfer_type'] = self.transfer_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntforestAccountTransferModel()
        if 'energy_account_from' in d:
            o.energy_account_from = d['energy_account_from']
        if 'energy_account_to' in d:
            o.energy_account_to = d['energy_account_to']
        if 'energy_count' in d:
            o.energy_count = d['energy_count']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'transfer_type' in d:
            o.transfer_type = d['transfer_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


