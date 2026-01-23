#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniReceiverAddressInfoDTO import MiniReceiverAddressInfoDTO
from alipay.aop.api.domain.AllocAmountInfoDTO import AllocAmountInfoDTO
from alipay.aop.api.domain.ContactInfoDTO import ContactInfoDTO
from alipay.aop.api.domain.CreditInfoDTO import CreditInfoDTO
from alipay.aop.api.domain.MiniReceiverAddressInfoDTO import MiniReceiverAddressInfoDTO
from alipay.aop.api.domain.LogisticsInfoDTO import LogisticsInfoDTO
from alipay.aop.api.domain.MiniOrderExtInfoDTO import MiniOrderExtInfoDTO
from alipay.aop.api.domain.MiniOrderDetailDTO import MiniOrderDetailDTO
from alipay.aop.api.domain.MiniOrderAddressInfoDTO import MiniOrderAddressInfoDTO
from alipay.aop.api.domain.ShopInfoDTO import ShopInfoDTO
from alipay.aop.api.domain.SubMerchantDTO import SubMerchantDTO


class OrderBuyDTO(object):

    def __init__(self):
        self._address_info = None
        self._alloc_amount_info = None
        self._confirm_timeout_express = None
        self._contact_info = None
        self._credit_info = None
        self._default_receiving_address = None
        self._delivery_detail = None
        self._ext_info = None
        self._memo = None
        self._merchant_biz_type = None
        self._order_detail = None
        self._out_order_id = None
        self._path = None
        self._seller_id = None
        self._send_address_info = None
        self._service_provider_model = None
        self._service_type = None
        self._shop_info = None
        self._sub_merchant = None
        self._title = None
        self._trade_app_id = None

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
    def alloc_amount_info(self):
        return self._alloc_amount_info

    @alloc_amount_info.setter
    def alloc_amount_info(self, value):
        if isinstance(value, AllocAmountInfoDTO):
            self._alloc_amount_info = value
        else:
            self._alloc_amount_info = AllocAmountInfoDTO.from_alipay_dict(value)
    @property
    def confirm_timeout_express(self):
        return self._confirm_timeout_express

    @confirm_timeout_express.setter
    def confirm_timeout_express(self, value):
        self._confirm_timeout_express = value
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
    def credit_info(self):
        return self._credit_info

    @credit_info.setter
    def credit_info(self, value):
        if isinstance(value, CreditInfoDTO):
            self._credit_info = value
        else:
            self._credit_info = CreditInfoDTO.from_alipay_dict(value)
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
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
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def send_address_info(self):
        return self._send_address_info

    @send_address_info.setter
    def send_address_info(self, value):
        if isinstance(value, MiniOrderAddressInfoDTO):
            self._send_address_info = value
        else:
            self._send_address_info = MiniOrderAddressInfoDTO.from_alipay_dict(value)
    @property
    def service_provider_model(self):
        return self._service_provider_model

    @service_provider_model.setter
    def service_provider_model(self, value):
        self._service_provider_model = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, ShopInfoDTO):
            self._shop_info = value
        else:
            self._shop_info = ShopInfoDTO.from_alipay_dict(value)
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchantDTO):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchantDTO.from_alipay_dict(value)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def trade_app_id(self):
        return self._trade_app_id

    @trade_app_id.setter
    def trade_app_id(self, value):
        self._trade_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.alloc_amount_info:
            if hasattr(self.alloc_amount_info, 'to_alipay_dict'):
                params['alloc_amount_info'] = self.alloc_amount_info.to_alipay_dict()
            else:
                params['alloc_amount_info'] = self.alloc_amount_info
        if self.confirm_timeout_express:
            if hasattr(self.confirm_timeout_express, 'to_alipay_dict'):
                params['confirm_timeout_express'] = self.confirm_timeout_express.to_alipay_dict()
            else:
                params['confirm_timeout_express'] = self.confirm_timeout_express
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.credit_info:
            if hasattr(self.credit_info, 'to_alipay_dict'):
                params['credit_info'] = self.credit_info.to_alipay_dict()
            else:
                params['credit_info'] = self.credit_info
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
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
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.send_address_info:
            if hasattr(self.send_address_info, 'to_alipay_dict'):
                params['send_address_info'] = self.send_address_info.to_alipay_dict()
            else:
                params['send_address_info'] = self.send_address_info
        if self.service_provider_model:
            if hasattr(self.service_provider_model, 'to_alipay_dict'):
                params['service_provider_model'] = self.service_provider_model.to_alipay_dict()
            else:
                params['service_provider_model'] = self.service_provider_model
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.trade_app_id:
            if hasattr(self.trade_app_id, 'to_alipay_dict'):
                params['trade_app_id'] = self.trade_app_id.to_alipay_dict()
            else:
                params['trade_app_id'] = self.trade_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderBuyDTO()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'alloc_amount_info' in d:
            o.alloc_amount_info = d['alloc_amount_info']
        if 'confirm_timeout_express' in d:
            o.confirm_timeout_express = d['confirm_timeout_express']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'credit_info' in d:
            o.credit_info = d['credit_info']
        if 'default_receiving_address' in d:
            o.default_receiving_address = d['default_receiving_address']
        if 'delivery_detail' in d:
            o.delivery_detail = d['delivery_detail']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_biz_type' in d:
            o.merchant_biz_type = d['merchant_biz_type']
        if 'order_detail' in d:
            o.order_detail = d['order_detail']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'path' in d:
            o.path = d['path']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'send_address_info' in d:
            o.send_address_info = d['send_address_info']
        if 'service_provider_model' in d:
            o.service_provider_model = d['service_provider_model']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'title' in d:
            o.title = d['title']
        if 'trade_app_id' in d:
            o.trade_app_id = d['trade_app_id']
        return o


