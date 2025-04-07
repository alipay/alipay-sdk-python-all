#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftCtocTransferQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._from_id_no = None
        self._from_id_type = None
        self._to_id_no = None
        self._to_id_type = None
        self._transfer_type = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def from_id_no(self):
        return self._from_id_no

    @from_id_no.setter
    def from_id_no(self, value):
        self._from_id_no = value
    @property
    def from_id_type(self):
        return self._from_id_type

    @from_id_type.setter
    def from_id_type(self, value):
        self._from_id_type = value
    @property
    def to_id_no(self):
        return self._to_id_no

    @to_id_no.setter
    def to_id_no(self, value):
        self._to_id_no = value
    @property
    def to_id_type(self):
        return self._to_id_type

    @to_id_type.setter
    def to_id_type(self, value):
        self._to_id_type = value
    @property
    def transfer_type(self):
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, value):
        self._transfer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.from_id_no:
            if hasattr(self.from_id_no, 'to_alipay_dict'):
                params['from_id_no'] = self.from_id_no.to_alipay_dict()
            else:
                params['from_id_no'] = self.from_id_no
        if self.from_id_type:
            if hasattr(self.from_id_type, 'to_alipay_dict'):
                params['from_id_type'] = self.from_id_type.to_alipay_dict()
            else:
                params['from_id_type'] = self.from_id_type
        if self.to_id_no:
            if hasattr(self.to_id_no, 'to_alipay_dict'):
                params['to_id_no'] = self.to_id_no.to_alipay_dict()
            else:
                params['to_id_no'] = self.to_id_no
        if self.to_id_type:
            if hasattr(self.to_id_type, 'to_alipay_dict'):
                params['to_id_type'] = self.to_id_type.to_alipay_dict()
            else:
                params['to_id_type'] = self.to_id_type
        if self.transfer_type:
            if hasattr(self.transfer_type, 'to_alipay_dict'):
                params['transfer_type'] = self.transfer_type.to_alipay_dict()
            else:
                params['transfer_type'] = self.transfer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftCtocTransferQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'from_id_no' in d:
            o.from_id_no = d['from_id_no']
        if 'from_id_type' in d:
            o.from_id_type = d['from_id_type']
        if 'to_id_no' in d:
            o.to_id_no = d['to_id_no']
        if 'to_id_type' in d:
            o.to_id_type = d['to_id_type']
        if 'transfer_type' in d:
            o.transfer_type = d['transfer_type']
        return o


