#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditGuaranteeSelleradmittanceQueryModel(object):

    def __init__(self):
        self._seller_login_id = None
        self._site = None

    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value


    def to_alipay_dict(self):
        params = dict()
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditGuaranteeSelleradmittanceQueryModel()
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'site' in d:
            o.site = d['site']
        return o


