#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentOrderReceiverAddressInfoDTO import RentOrderReceiverAddressInfoDTO
from alipay.aop.api.domain.RentBuyerIdentityInfo import RentBuyerIdentityInfo
from alipay.aop.api.domain.RentOrderReceiverAddressInfoDTO import RentOrderReceiverAddressInfoDTO
from alipay.aop.api.domain.RentOrderDeliveryInfoDTO import RentOrderDeliveryInfoDTO
from alipay.aop.api.domain.RentGoodsDetailInfoDTO import RentGoodsDetailInfoDTO
from alipay.aop.api.domain.RentOrderPriceInfoDTO import RentOrderPriceInfoDTO
from alipay.aop.api.domain.RentPlanInfoDTO import RentPlanInfoDTO
from alipay.aop.api.domain.RentSignInfoDTO import RentSignInfoDTO
from alipay.aop.api.domain.RentSubMerchantDTO import RentSubMerchantDTO


class AlipayCommerceRentOrderPrecreateModel(object):

    def __init__(self):
        self._activity_consult_id = None
        self._address_info = None
        self._buyer_identity_info = None
        self._cancel_back_link = None
        self._default_receiving_address = None
        self._delivery_info = None
        self._extend_params = None
        self._item_infos = None
        self._memo = None
        self._out_order_id = None
        self._out_order_source = None
        self._price_info = None
        self._rent_plan_info = None
        self._rent_sign_info = None
        self._return_back_link = None
        self._sub_merchant = None
        self._title = None
        self._trade_app_id = None

    @property
    def activity_consult_id(self):
        return self._activity_consult_id

    @activity_consult_id.setter
    def activity_consult_id(self, value):
        self._activity_consult_id = value
    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RentOrderReceiverAddressInfoDTO):
            self._address_info = value
        else:
            self._address_info = RentOrderReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def buyer_identity_info(self):
        return self._buyer_identity_info

    @buyer_identity_info.setter
    def buyer_identity_info(self, value):
        if isinstance(value, RentBuyerIdentityInfo):
            self._buyer_identity_info = value
        else:
            self._buyer_identity_info = RentBuyerIdentityInfo.from_alipay_dict(value)
    @property
    def cancel_back_link(self):
        return self._cancel_back_link

    @cancel_back_link.setter
    def cancel_back_link(self, value):
        self._cancel_back_link = value
    @property
    def default_receiving_address(self):
        return self._default_receiving_address

    @default_receiving_address.setter
    def default_receiving_address(self, value):
        if isinstance(value, RentOrderReceiverAddressInfoDTO):
            self._default_receiving_address = value
        else:
            self._default_receiving_address = RentOrderReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, RentOrderDeliveryInfoDTO):
            self._delivery_info = value
        else:
            self._delivery_info = RentOrderDeliveryInfoDTO.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, RentGoodsDetailInfoDTO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(RentGoodsDetailInfoDTO.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_order_source(self):
        return self._out_order_source

    @out_order_source.setter
    def out_order_source(self, value):
        self._out_order_source = value
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, RentOrderPriceInfoDTO):
            self._price_info = value
        else:
            self._price_info = RentOrderPriceInfoDTO.from_alipay_dict(value)
    @property
    def rent_plan_info(self):
        return self._rent_plan_info

    @rent_plan_info.setter
    def rent_plan_info(self, value):
        if isinstance(value, RentPlanInfoDTO):
            self._rent_plan_info = value
        else:
            self._rent_plan_info = RentPlanInfoDTO.from_alipay_dict(value)
    @property
    def rent_sign_info(self):
        return self._rent_sign_info

    @rent_sign_info.setter
    def rent_sign_info(self, value):
        if isinstance(value, RentSignInfoDTO):
            self._rent_sign_info = value
        else:
            self._rent_sign_info = RentSignInfoDTO.from_alipay_dict(value)
    @property
    def return_back_link(self):
        return self._return_back_link

    @return_back_link.setter
    def return_back_link(self, value):
        self._return_back_link = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, RentSubMerchantDTO):
            self._sub_merchant = value
        else:
            self._sub_merchant = RentSubMerchantDTO.from_alipay_dict(value)
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
        if self.activity_consult_id:
            if hasattr(self.activity_consult_id, 'to_alipay_dict'):
                params['activity_consult_id'] = self.activity_consult_id.to_alipay_dict()
            else:
                params['activity_consult_id'] = self.activity_consult_id
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.buyer_identity_info:
            if hasattr(self.buyer_identity_info, 'to_alipay_dict'):
                params['buyer_identity_info'] = self.buyer_identity_info.to_alipay_dict()
            else:
                params['buyer_identity_info'] = self.buyer_identity_info
        if self.cancel_back_link:
            if hasattr(self.cancel_back_link, 'to_alipay_dict'):
                params['cancel_back_link'] = self.cancel_back_link.to_alipay_dict()
            else:
                params['cancel_back_link'] = self.cancel_back_link
        if self.default_receiving_address:
            if hasattr(self.default_receiving_address, 'to_alipay_dict'):
                params['default_receiving_address'] = self.default_receiving_address.to_alipay_dict()
            else:
                params['default_receiving_address'] = self.default_receiving_address
        if self.delivery_info:
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_order_source:
            if hasattr(self.out_order_source, 'to_alipay_dict'):
                params['out_order_source'] = self.out_order_source.to_alipay_dict()
            else:
                params['out_order_source'] = self.out_order_source
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.rent_plan_info:
            if hasattr(self.rent_plan_info, 'to_alipay_dict'):
                params['rent_plan_info'] = self.rent_plan_info.to_alipay_dict()
            else:
                params['rent_plan_info'] = self.rent_plan_info
        if self.rent_sign_info:
            if hasattr(self.rent_sign_info, 'to_alipay_dict'):
                params['rent_sign_info'] = self.rent_sign_info.to_alipay_dict()
            else:
                params['rent_sign_info'] = self.rent_sign_info
        if self.return_back_link:
            if hasattr(self.return_back_link, 'to_alipay_dict'):
                params['return_back_link'] = self.return_back_link.to_alipay_dict()
            else:
                params['return_back_link'] = self.return_back_link
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
        o = AlipayCommerceRentOrderPrecreateModel()
        if 'activity_consult_id' in d:
            o.activity_consult_id = d['activity_consult_id']
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'buyer_identity_info' in d:
            o.buyer_identity_info = d['buyer_identity_info']
        if 'cancel_back_link' in d:
            o.cancel_back_link = d['cancel_back_link']
        if 'default_receiving_address' in d:
            o.default_receiving_address = d['default_receiving_address']
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_order_source' in d:
            o.out_order_source = d['out_order_source']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'rent_plan_info' in d:
            o.rent_plan_info = d['rent_plan_info']
        if 'rent_sign_info' in d:
            o.rent_sign_info = d['rent_sign_info']
        if 'return_back_link' in d:
            o.return_back_link = d['return_back_link']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'title' in d:
            o.title = d['title']
        if 'trade_app_id' in d:
            o.trade_app_id = d['trade_app_id']
        return o


