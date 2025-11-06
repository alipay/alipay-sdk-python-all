#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniCertificateUseInfo import MiniCertificateUseInfo
from alipay.aop.api.domain.MiniItemInfo import MiniItemInfo
from alipay.aop.api.domain.OrderBaseInfo import OrderBaseInfo
from alipay.aop.api.domain.MiniPriceInfoDTO import MiniPriceInfoDTO
from alipay.aop.api.domain.MiniRefundInfo import MiniRefundInfo
from alipay.aop.api.domain.MiniStatusInfo import MiniStatusInfo
from alipay.aop.api.domain.MiniUserInfo import MiniUserInfo


class CertificateUseInfoDTO(object):

    def __init__(self):
        self._certificate_use_info = None
        self._item_info = None
        self._order_base_info = None
        self._price_info = None
        self._refund_info = None
        self._status_info = None
        self._user_info = None

    @property
    def certificate_use_info(self):
        return self._certificate_use_info

    @certificate_use_info.setter
    def certificate_use_info(self, value):
        if isinstance(value, MiniCertificateUseInfo):
            self._certificate_use_info = value
        else:
            self._certificate_use_info = MiniCertificateUseInfo.from_alipay_dict(value)
    @property
    def item_info(self):
        return self._item_info

    @item_info.setter
    def item_info(self, value):
        if isinstance(value, MiniItemInfo):
            self._item_info = value
        else:
            self._item_info = MiniItemInfo.from_alipay_dict(value)
    @property
    def order_base_info(self):
        return self._order_base_info

    @order_base_info.setter
    def order_base_info(self, value):
        if isinstance(value, OrderBaseInfo):
            self._order_base_info = value
        else:
            self._order_base_info = OrderBaseInfo.from_alipay_dict(value)
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, MiniPriceInfoDTO):
            self._price_info = value
        else:
            self._price_info = MiniPriceInfoDTO.from_alipay_dict(value)
    @property
    def refund_info(self):
        return self._refund_info

    @refund_info.setter
    def refund_info(self, value):
        if isinstance(value, MiniRefundInfo):
            self._refund_info = value
        else:
            self._refund_info = MiniRefundInfo.from_alipay_dict(value)
    @property
    def status_info(self):
        return self._status_info

    @status_info.setter
    def status_info(self, value):
        if isinstance(value, MiniStatusInfo):
            self._status_info = value
        else:
            self._status_info = MiniStatusInfo.from_alipay_dict(value)
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, MiniUserInfo):
            self._user_info = value
        else:
            self._user_info = MiniUserInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_use_info:
            if hasattr(self.certificate_use_info, 'to_alipay_dict'):
                params['certificate_use_info'] = self.certificate_use_info.to_alipay_dict()
            else:
                params['certificate_use_info'] = self.certificate_use_info
        if self.item_info:
            if hasattr(self.item_info, 'to_alipay_dict'):
                params['item_info'] = self.item_info.to_alipay_dict()
            else:
                params['item_info'] = self.item_info
        if self.order_base_info:
            if hasattr(self.order_base_info, 'to_alipay_dict'):
                params['order_base_info'] = self.order_base_info.to_alipay_dict()
            else:
                params['order_base_info'] = self.order_base_info
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.refund_info:
            if hasattr(self.refund_info, 'to_alipay_dict'):
                params['refund_info'] = self.refund_info.to_alipay_dict()
            else:
                params['refund_info'] = self.refund_info
        if self.status_info:
            if hasattr(self.status_info, 'to_alipay_dict'):
                params['status_info'] = self.status_info.to_alipay_dict()
            else:
                params['status_info'] = self.status_info
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateUseInfoDTO()
        if 'certificate_use_info' in d:
            o.certificate_use_info = d['certificate_use_info']
        if 'item_info' in d:
            o.item_info = d['item_info']
        if 'order_base_info' in d:
            o.order_base_info = d['order_base_info']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'refund_info' in d:
            o.refund_info = d['refund_info']
        if 'status_info' in d:
            o.status_info = d['status_info']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


