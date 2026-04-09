#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EscrowBusinessInfo import EscrowBusinessInfo
from alipay.aop.api.domain.EscrowSettleCardInfo import EscrowSettleCardInfo
from alipay.aop.api.domain.EscrowContactInfo import EscrowContactInfo
from alipay.aop.api.domain.EscrowLicense import EscrowLicense


class AntMerchantEscrowApplyModel(object):

    def __init__(self):
        self._business_info = None
        self._card_info = None
        self._contact_info = None
        self._license = None
        self._out_request_no = None
        self._platform_partner_id = None
        self._seller_shop_name = None
        self._seller_type = None
        self._seller_user_id = None
        self._seller_user_name = None

    @property
    def business_info(self):
        return self._business_info

    @business_info.setter
    def business_info(self, value):
        if isinstance(value, EscrowBusinessInfo):
            self._business_info = value
        else:
            self._business_info = EscrowBusinessInfo.from_alipay_dict(value)
    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, EscrowSettleCardInfo):
            self._card_info = value
        else:
            self._card_info = EscrowSettleCardInfo.from_alipay_dict(value)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, EscrowContactInfo):
            self._contact_info = value
        else:
            self._contact_info = EscrowContactInfo.from_alipay_dict(value)
    @property
    def license(self):
        return self._license

    @license.setter
    def license(self, value):
        if isinstance(value, EscrowLicense):
            self._license = value
        else:
            self._license = EscrowLicense.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def platform_partner_id(self):
        return self._platform_partner_id

    @platform_partner_id.setter
    def platform_partner_id(self, value):
        self._platform_partner_id = value
    @property
    def seller_shop_name(self):
        return self._seller_shop_name

    @seller_shop_name.setter
    def seller_shop_name(self, value):
        self._seller_shop_name = value
    @property
    def seller_type(self):
        return self._seller_type

    @seller_type.setter
    def seller_type(self, value):
        self._seller_type = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def seller_user_name(self):
        return self._seller_user_name

    @seller_user_name.setter
    def seller_user_name(self, value):
        self._seller_user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_info:
            if hasattr(self.business_info, 'to_alipay_dict'):
                params['business_info'] = self.business_info.to_alipay_dict()
            else:
                params['business_info'] = self.business_info
        if self.card_info:
            if hasattr(self.card_info, 'to_alipay_dict'):
                params['card_info'] = self.card_info.to_alipay_dict()
            else:
                params['card_info'] = self.card_info
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.license:
            if hasattr(self.license, 'to_alipay_dict'):
                params['license'] = self.license.to_alipay_dict()
            else:
                params['license'] = self.license
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.platform_partner_id:
            if hasattr(self.platform_partner_id, 'to_alipay_dict'):
                params['platform_partner_id'] = self.platform_partner_id.to_alipay_dict()
            else:
                params['platform_partner_id'] = self.platform_partner_id
        if self.seller_shop_name:
            if hasattr(self.seller_shop_name, 'to_alipay_dict'):
                params['seller_shop_name'] = self.seller_shop_name.to_alipay_dict()
            else:
                params['seller_shop_name'] = self.seller_shop_name
        if self.seller_type:
            if hasattr(self.seller_type, 'to_alipay_dict'):
                params['seller_type'] = self.seller_type.to_alipay_dict()
            else:
                params['seller_type'] = self.seller_type
        if self.seller_user_id:
            if hasattr(self.seller_user_id, 'to_alipay_dict'):
                params['seller_user_id'] = self.seller_user_id.to_alipay_dict()
            else:
                params['seller_user_id'] = self.seller_user_id
        if self.seller_user_name:
            if hasattr(self.seller_user_name, 'to_alipay_dict'):
                params['seller_user_name'] = self.seller_user_name.to_alipay_dict()
            else:
                params['seller_user_name'] = self.seller_user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantEscrowApplyModel()
        if 'business_info' in d:
            o.business_info = d['business_info']
        if 'card_info' in d:
            o.card_info = d['card_info']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'license' in d:
            o.license = d['license']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'platform_partner_id' in d:
            o.platform_partner_id = d['platform_partner_id']
        if 'seller_shop_name' in d:
            o.seller_shop_name = d['seller_shop_name']
        if 'seller_type' in d:
            o.seller_type = d['seller_type']
        if 'seller_user_id' in d:
            o.seller_user_id = d['seller_user_id']
        if 'seller_user_name' in d:
            o.seller_user_name = d['seller_user_name']
        return o


