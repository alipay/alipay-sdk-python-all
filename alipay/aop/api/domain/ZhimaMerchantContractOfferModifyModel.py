#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantContractOfferModifyModel(object):

    def __init__(self):
        self._contract_content = None
        self._contract_principal_desc = None
        self._contract_principal_logo = None
        self._fufilment_callback_url = None
        self._fufilment_desc = None
        self._offer_creater_id = None
        self._offer_creater_type = None
        self._offer_no = None
        self._service_id = None

    @property
    def contract_content(self):
        return self._contract_content

    @contract_content.setter
    def contract_content(self, value):
        self._contract_content = value
    @property
    def contract_principal_desc(self):
        return self._contract_principal_desc

    @contract_principal_desc.setter
    def contract_principal_desc(self, value):
        self._contract_principal_desc = value
    @property
    def contract_principal_logo(self):
        return self._contract_principal_logo

    @contract_principal_logo.setter
    def contract_principal_logo(self, value):
        self._contract_principal_logo = value
    @property
    def fufilment_callback_url(self):
        return self._fufilment_callback_url

    @fufilment_callback_url.setter
    def fufilment_callback_url(self, value):
        self._fufilment_callback_url = value
    @property
    def fufilment_desc(self):
        return self._fufilment_desc

    @fufilment_desc.setter
    def fufilment_desc(self, value):
        self._fufilment_desc = value
    @property
    def offer_creater_id(self):
        return self._offer_creater_id

    @offer_creater_id.setter
    def offer_creater_id(self, value):
        self._offer_creater_id = value
    @property
    def offer_creater_type(self):
        return self._offer_creater_type

    @offer_creater_type.setter
    def offer_creater_type(self, value):
        self._offer_creater_type = value
    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_content:
            if hasattr(self.contract_content, 'to_alipay_dict'):
                params['contract_content'] = self.contract_content.to_alipay_dict()
            else:
                params['contract_content'] = self.contract_content
        if self.contract_principal_desc:
            if hasattr(self.contract_principal_desc, 'to_alipay_dict'):
                params['contract_principal_desc'] = self.contract_principal_desc.to_alipay_dict()
            else:
                params['contract_principal_desc'] = self.contract_principal_desc
        if self.contract_principal_logo:
            if hasattr(self.contract_principal_logo, 'to_alipay_dict'):
                params['contract_principal_logo'] = self.contract_principal_logo.to_alipay_dict()
            else:
                params['contract_principal_logo'] = self.contract_principal_logo
        if self.fufilment_callback_url:
            if hasattr(self.fufilment_callback_url, 'to_alipay_dict'):
                params['fufilment_callback_url'] = self.fufilment_callback_url.to_alipay_dict()
            else:
                params['fufilment_callback_url'] = self.fufilment_callback_url
        if self.fufilment_desc:
            if hasattr(self.fufilment_desc, 'to_alipay_dict'):
                params['fufilment_desc'] = self.fufilment_desc.to_alipay_dict()
            else:
                params['fufilment_desc'] = self.fufilment_desc
        if self.offer_creater_id:
            if hasattr(self.offer_creater_id, 'to_alipay_dict'):
                params['offer_creater_id'] = self.offer_creater_id.to_alipay_dict()
            else:
                params['offer_creater_id'] = self.offer_creater_id
        if self.offer_creater_type:
            if hasattr(self.offer_creater_type, 'to_alipay_dict'):
                params['offer_creater_type'] = self.offer_creater_type.to_alipay_dict()
            else:
                params['offer_creater_type'] = self.offer_creater_type
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantContractOfferModifyModel()
        if 'contract_content' in d:
            o.contract_content = d['contract_content']
        if 'contract_principal_desc' in d:
            o.contract_principal_desc = d['contract_principal_desc']
        if 'contract_principal_logo' in d:
            o.contract_principal_logo = d['contract_principal_logo']
        if 'fufilment_callback_url' in d:
            o.fufilment_callback_url = d['fufilment_callback_url']
        if 'fufilment_desc' in d:
            o.fufilment_desc = d['fufilment_desc']
        if 'offer_creater_id' in d:
            o.offer_creater_id = d['offer_creater_id']
        if 'offer_creater_type' in d:
            o.offer_creater_type = d['offer_creater_type']
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


