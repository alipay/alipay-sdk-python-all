#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniReceiverAddressInfoDTO import MiniReceiverAddressInfoDTO
from alipay.aop.api.domain.MiniBusinessParamsDTO import MiniBusinessParamsDTO
from alipay.aop.api.domain.ContactInfoDTO import ContactInfoDTO
from alipay.aop.api.domain.MiniReceiverAddressInfoDTO import MiniReceiverAddressInfoDTO
from alipay.aop.api.domain.LogisticsInfoDTO import LogisticsInfoDTO
from alipay.aop.api.domain.MiniOrderExtInfoDTO import MiniOrderExtInfoDTO
from alipay.aop.api.domain.MiniOrderDetailDTO import MiniOrderDetailDTO
from alipay.aop.api.domain.PromoDetailInfoDTO import PromoDetailInfoDTO


class AlipayOpenMiniOrderCreateModel(object):

    def __init__(self):
        self._address_info = None
        self._business_params = None
        self._buyer_id = None
        self._buyer_logon_id = None
        self._buyer_open_id = None
        self._contact_info = None
        self._default_receiving_address = None
        self._delivery_detail = None
        self._ext_info = None
        self._merchant_biz_type = None
        self._order_detail = None
        self._out_order_id = None
        self._path = None
        self._promo_detail_info = None
        self._seller_id = None
        self._source_id = None
        self._timeout_express = None
        self._title = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, MiniReceiverAddressInfoDTO):
            self._address_info = value
        else:
            self._address_info = MiniReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, MiniBusinessParamsDTO):
            self._business_params = value
        else:
            self._business_params = MiniBusinessParamsDTO.from_alipay_dict(value)
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, ContactInfoDTO):
            self._contact_info = value
        else:
            self._contact_info = ContactInfoDTO.from_alipay_dict(value)
    @property
    def default_receiving_address(self):
        return self._default_receiving_address

    @default_receiving_address.setter
    def default_receiving_address(self, value):
        if isinstance(value, MiniReceiverAddressInfoDTO):
            self._default_receiving_address = value
        else:
            self._default_receiving_address = MiniReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def delivery_detail(self):
        return self._delivery_detail

    @delivery_detail.setter
    def delivery_detail(self, value):
        if isinstance(value, LogisticsInfoDTO):
            self._delivery_detail = value
        else:
            self._delivery_detail = LogisticsInfoDTO.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, MiniOrderExtInfoDTO):
            self._ext_info = value
        else:
            self._ext_info = MiniOrderExtInfoDTO.from_alipay_dict(value)
    @property
    def merchant_biz_type(self):
        return self._merchant_biz_type

    @merchant_biz_type.setter
    def merchant_biz_type(self, value):
        self._merchant_biz_type = value
    @property
    def order_detail(self):
        return self._order_detail

    @order_detail.setter
    def order_detail(self, value):
        if isinstance(value, MiniOrderDetailDTO):
            self._order_detail = value
        else:
            self._order_detail = MiniOrderDetailDTO.from_alipay_dict(value)
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def promo_detail_info(self):
        return self._promo_detail_info

    @promo_detail_info.setter
    def promo_detail_info(self, value):
        if isinstance(value, PromoDetailInfoDTO):
            self._promo_detail_info = value
        else:
            self._promo_detail_info = PromoDetailInfoDTO.from_alipay_dict(value)
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_logon_id:
            if hasattr(self.buyer_logon_id, 'to_alipay_dict'):
                params['buyer_logon_id'] = self.buyer_logon_id.to_alipay_dict()
            else:
                params['buyer_logon_id'] = self.buyer_logon_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.default_receiving_address:
            if hasattr(self.default_receiving_address, 'to_alipay_dict'):
                params['default_receiving_address'] = self.default_receiving_address.to_alipay_dict()
            else:
                params['default_receiving_address'] = self.default_receiving_address
        if self.delivery_detail:
            if hasattr(self.delivery_detail, 'to_alipay_dict'):
                params['delivery_detail'] = self.delivery_detail.to_alipay_dict()
            else:
                params['delivery_detail'] = self.delivery_detail
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_biz_type:
            if hasattr(self.merchant_biz_type, 'to_alipay_dict'):
                params['merchant_biz_type'] = self.merchant_biz_type.to_alipay_dict()
            else:
                params['merchant_biz_type'] = self.merchant_biz_type
        if self.order_detail:
            if hasattr(self.order_detail, 'to_alipay_dict'):
                params['order_detail'] = self.order_detail.to_alipay_dict()
            else:
                params['order_detail'] = self.order_detail
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.promo_detail_info:
            if hasattr(self.promo_detail_info, 'to_alipay_dict'):
                params['promo_detail_info'] = self.promo_detail_info.to_alipay_dict()
            else:
                params['promo_detail_info'] = self.promo_detail_info
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderCreateModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_logon_id' in d:
            o.buyer_logon_id = d['buyer_logon_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'default_receiving_address' in d:
            o.default_receiving_address = d['default_receiving_address']
        if 'delivery_detail' in d:
            o.delivery_detail = d['delivery_detail']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_biz_type' in d:
            o.merchant_biz_type = d['merchant_biz_type']
        if 'order_detail' in d:
            o.order_detail = d['order_detail']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'path' in d:
            o.path = d['path']
        if 'promo_detail_info' in d:
            o.promo_detail_info = d['promo_detail_info']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'title' in d:
            o.title = d['title']
        return o


