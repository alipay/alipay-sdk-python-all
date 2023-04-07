#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsContactAddressDTO import LogisticsContactAddressDTO
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO
from alipay.aop.api.domain.LogisticsContactAddressDTO import LogisticsContactAddressDTO


class AlipayInsSceneEcommerceHomedeliverylinkAuthModel(object):

    def __init__(self):
        self._buyer_contact_address = None
        self._buyer_id = None
        self._order_dto = None
        self._out_session_expiration = None
        self._out_session_id = None
        self._partner_org_id = None
        self._refund_status = None
        self._related_policy_no = None
        self._seller_agree_refund_time = None
        self._seller_contact_address = None
        self._user_client = None

    @property
    def buyer_contact_address(self):
        return self._buyer_contact_address

    @buyer_contact_address.setter
    def buyer_contact_address(self, value):
        if isinstance(value, LogisticsContactAddressDTO):
            self._buyer_contact_address = value
        else:
            self._buyer_contact_address = LogisticsContactAddressDTO.from_alipay_dict(value)
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def order_dto(self):
        return self._order_dto

    @order_dto.setter
    def order_dto(self, value):
        if isinstance(value, EcomOrderDTO):
            self._order_dto = value
        else:
            self._order_dto = EcomOrderDTO.from_alipay_dict(value)
    @property
    def out_session_expiration(self):
        return self._out_session_expiration

    @out_session_expiration.setter
    def out_session_expiration(self, value):
        self._out_session_expiration = value
    @property
    def out_session_id(self):
        return self._out_session_id

    @out_session_id.setter
    def out_session_id(self, value):
        self._out_session_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def related_policy_no(self):
        return self._related_policy_no

    @related_policy_no.setter
    def related_policy_no(self, value):
        self._related_policy_no = value
    @property
    def seller_agree_refund_time(self):
        return self._seller_agree_refund_time

    @seller_agree_refund_time.setter
    def seller_agree_refund_time(self, value):
        self._seller_agree_refund_time = value
    @property
    def seller_contact_address(self):
        return self._seller_contact_address

    @seller_contact_address.setter
    def seller_contact_address(self, value):
        if isinstance(value, LogisticsContactAddressDTO):
            self._seller_contact_address = value
        else:
            self._seller_contact_address = LogisticsContactAddressDTO.from_alipay_dict(value)
    @property
    def user_client(self):
        return self._user_client

    @user_client.setter
    def user_client(self, value):
        self._user_client = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_contact_address:
            if hasattr(self.buyer_contact_address, 'to_alipay_dict'):
                params['buyer_contact_address'] = self.buyer_contact_address.to_alipay_dict()
            else:
                params['buyer_contact_address'] = self.buyer_contact_address
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.order_dto:
            if hasattr(self.order_dto, 'to_alipay_dict'):
                params['order_dto'] = self.order_dto.to_alipay_dict()
            else:
                params['order_dto'] = self.order_dto
        if self.out_session_expiration:
            if hasattr(self.out_session_expiration, 'to_alipay_dict'):
                params['out_session_expiration'] = self.out_session_expiration.to_alipay_dict()
            else:
                params['out_session_expiration'] = self.out_session_expiration
        if self.out_session_id:
            if hasattr(self.out_session_id, 'to_alipay_dict'):
                params['out_session_id'] = self.out_session_id.to_alipay_dict()
            else:
                params['out_session_id'] = self.out_session_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.related_policy_no:
            if hasattr(self.related_policy_no, 'to_alipay_dict'):
                params['related_policy_no'] = self.related_policy_no.to_alipay_dict()
            else:
                params['related_policy_no'] = self.related_policy_no
        if self.seller_agree_refund_time:
            if hasattr(self.seller_agree_refund_time, 'to_alipay_dict'):
                params['seller_agree_refund_time'] = self.seller_agree_refund_time.to_alipay_dict()
            else:
                params['seller_agree_refund_time'] = self.seller_agree_refund_time
        if self.seller_contact_address:
            if hasattr(self.seller_contact_address, 'to_alipay_dict'):
                params['seller_contact_address'] = self.seller_contact_address.to_alipay_dict()
            else:
                params['seller_contact_address'] = self.seller_contact_address
        if self.user_client:
            if hasattr(self.user_client, 'to_alipay_dict'):
                params['user_client'] = self.user_client.to_alipay_dict()
            else:
                params['user_client'] = self.user_client
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEcommerceHomedeliverylinkAuthModel()
        if 'buyer_contact_address' in d:
            o.buyer_contact_address = d['buyer_contact_address']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'order_dto' in d:
            o.order_dto = d['order_dto']
        if 'out_session_expiration' in d:
            o.out_session_expiration = d['out_session_expiration']
        if 'out_session_id' in d:
            o.out_session_id = d['out_session_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'related_policy_no' in d:
            o.related_policy_no = d['related_policy_no']
        if 'seller_agree_refund_time' in d:
            o.seller_agree_refund_time = d['seller_agree_refund_time']
        if 'seller_contact_address' in d:
            o.seller_contact_address = d['seller_contact_address']
        if 'user_client' in d:
            o.user_client = d['user_client']
        return o


