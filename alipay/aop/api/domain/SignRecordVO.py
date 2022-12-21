#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignRecordLogVO import SignRecordLogVO


class SignRecordVO(object):

    def __init__(self):
        self._agreement_id = None
        self._log_vos = None
        self._out_sign_no = None
        self._product_cd = None
        self._status = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def log_vos(self):
        return self._log_vos

    @log_vos.setter
    def log_vos(self, value):
        if isinstance(value, list):
            self._log_vos = list()
            for i in value:
                if isinstance(i, SignRecordLogVO):
                    self._log_vos.append(i)
                else:
                    self._log_vos.append(SignRecordLogVO.from_alipay_dict(i))
    @property
    def out_sign_no(self):
        return self._out_sign_no

    @out_sign_no.setter
    def out_sign_no(self, value):
        self._out_sign_no = value
    @property
    def product_cd(self):
        return self._product_cd

    @product_cd.setter
    def product_cd(self, value):
        self._product_cd = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.log_vos:
            if isinstance(self.log_vos, list):
                for i in range(0, len(self.log_vos)):
                    element = self.log_vos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.log_vos[i] = element.to_alipay_dict()
            if hasattr(self.log_vos, 'to_alipay_dict'):
                params['log_vos'] = self.log_vos.to_alipay_dict()
            else:
                params['log_vos'] = self.log_vos
        if self.out_sign_no:
            if hasattr(self.out_sign_no, 'to_alipay_dict'):
                params['out_sign_no'] = self.out_sign_no.to_alipay_dict()
            else:
                params['out_sign_no'] = self.out_sign_no
        if self.product_cd:
            if hasattr(self.product_cd, 'to_alipay_dict'):
                params['product_cd'] = self.product_cd.to_alipay_dict()
            else:
                params['product_cd'] = self.product_cd
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignRecordVO()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'log_vos' in d:
            o.log_vos = d['log_vos']
        if 'out_sign_no' in d:
            o.out_sign_no = d['out_sign_no']
        if 'product_cd' in d:
            o.product_cd = d['product_cd']
        if 'status' in d:
            o.status = d['status']
        return o


