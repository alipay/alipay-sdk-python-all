#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAlcagmprodAgreementUnsignModel(object):

    def __init__(self):
        self._agreement_id_list = None
        self._cancel_date = None
        self._out_sign_no = None
        self._product_cd = None
        self._request_from = None
        self._request_no = None
        self._user_id = None

    @property
    def agreement_id_list(self):
        return self._agreement_id_list

    @agreement_id_list.setter
    def agreement_id_list(self, value):
        if isinstance(value, list):
            self._agreement_id_list = list()
            for i in value:
                self._agreement_id_list.append(i)
    @property
    def cancel_date(self):
        return self._cancel_date

    @cancel_date.setter
    def cancel_date(self, value):
        self._cancel_date = value
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
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id_list:
            if isinstance(self.agreement_id_list, list):
                for i in range(0, len(self.agreement_id_list)):
                    element = self.agreement_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_id_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_id_list, 'to_alipay_dict'):
                params['agreement_id_list'] = self.agreement_id_list.to_alipay_dict()
            else:
                params['agreement_id_list'] = self.agreement_id_list
        if self.cancel_date:
            if hasattr(self.cancel_date, 'to_alipay_dict'):
                params['cancel_date'] = self.cancel_date.to_alipay_dict()
            else:
                params['cancel_date'] = self.cancel_date
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
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
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
        o = AlipayBossProdAlcagmprodAgreementUnsignModel()
        if 'agreement_id_list' in d:
            o.agreement_id_list = d['agreement_id_list']
        if 'cancel_date' in d:
            o.cancel_date = d['cancel_date']
        if 'out_sign_no' in d:
            o.out_sign_no = d['out_sign_no']
        if 'product_cd' in d:
            o.product_cd = d['product_cd']
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


