#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentOrderReceiverAddressInfoDTO import RentOrderReceiverAddressInfoDTO
from alipay.aop.api.domain.RentBuyoutInfoDTO import RentBuyoutInfoDTO
from alipay.aop.api.domain.RentOrderReceiverAddressInfoDTO import RentOrderReceiverAddressInfoDTO
from alipay.aop.api.domain.RentOrderDeliveryInfoDTO import RentOrderDeliveryInfoDTO
from alipay.aop.api.domain.RentGoodsDetailInfoDTO import RentGoodsDetailInfoDTO
from alipay.aop.api.domain.RentOfflineShoppingDTO import RentOfflineShoppingDTO
from alipay.aop.api.domain.RentPathInfoDTO import RentPathInfoDTO
from alipay.aop.api.domain.RentOrderPriceInfoDTO import RentOrderPriceInfoDTO
from alipay.aop.api.domain.RentReletInfoDTO import RentReletInfoDTO
from alipay.aop.api.domain.RentPlanInfoDTO import RentPlanInfoDTO
from alipay.aop.api.domain.RentSignInfoDTO import RentSignInfoDTO
from alipay.aop.api.domain.RentSubMerchantDTO import RentSubMerchantDTO
from alipay.aop.api.domain.RentZstInfoDTO import RentZstInfoDTO


class AlipayCommerceRentOrderCreateModel(object):

    def __init__(self):
        self._activity_consult_id = None
        self._address_info = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._buyout_info = None
        self._buyout_installment_no = None
        self._default_receiving_address = None
        self._delivery_info = None
        self._item_infos = None
        self._memo = None
        self._offline_shopping_info = None
        self._order_type = None
        self._out_order_id = None
        self._parent_order_id = None
        self._path_info = None
        self._price_info = None
        self._relet_info = None
        self._rent_plan_info = None
        self._rent_sign_info = None
        self._service_provider_model = None
        self._source_id = None
        self._sub_merchant = None
        self._title = None
        self._trade_app_id = None
        self._zst_info = None

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
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyout_info(self):
        return self._buyout_info

    @buyout_info.setter
    def buyout_info(self, value):
        if isinstance(value, RentBuyoutInfoDTO):
            self._buyout_info = value
        else:
            self._buyout_info = RentBuyoutInfoDTO.from_alipay_dict(value)
    @property
    def buyout_installment_no(self):
        return self._buyout_installment_no

    @buyout_installment_no.setter
    def buyout_installment_no(self, value):
        self._buyout_installment_no = value
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
    def offline_shopping_info(self):
        return self._offline_shopping_info

    @offline_shopping_info.setter
    def offline_shopping_info(self, value):
        if isinstance(value, RentOfflineShoppingDTO):
            self._offline_shopping_info = value
        else:
            self._offline_shopping_info = RentOfflineShoppingDTO.from_alipay_dict(value)
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def parent_order_id(self):
        return self._parent_order_id

    @parent_order_id.setter
    def parent_order_id(self, value):
        self._parent_order_id = value
    @property
    def path_info(self):
        return self._path_info

    @path_info.setter
    def path_info(self, value):
        if isinstance(value, RentPathInfoDTO):
            self._path_info = value
        else:
            self._path_info = RentPathInfoDTO.from_alipay_dict(value)
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
    def relet_info(self):
        return self._relet_info

    @relet_info.setter
    def relet_info(self, value):
        if isinstance(value, RentReletInfoDTO):
            self._relet_info = value
        else:
            self._relet_info = RentReletInfoDTO.from_alipay_dict(value)
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
    def service_provider_model(self):
        return self._service_provider_model

    @service_provider_model.setter
    def service_provider_model(self, value):
        self._service_provider_model = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
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
    @property
    def zst_info(self):
        return self._zst_info

    @zst_info.setter
    def zst_info(self, value):
        if isinstance(value, RentZstInfoDTO):
            self._zst_info = value
        else:
            self._zst_info = RentZstInfoDTO.from_alipay_dict(value)


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
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.buyout_info:
            if hasattr(self.buyout_info, 'to_alipay_dict'):
                params['buyout_info'] = self.buyout_info.to_alipay_dict()
            else:
                params['buyout_info'] = self.buyout_info
        if self.buyout_installment_no:
            if hasattr(self.buyout_installment_no, 'to_alipay_dict'):
                params['buyout_installment_no'] = self.buyout_installment_no.to_alipay_dict()
            else:
                params['buyout_installment_no'] = self.buyout_installment_no
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
        if self.offline_shopping_info:
            if hasattr(self.offline_shopping_info, 'to_alipay_dict'):
                params['offline_shopping_info'] = self.offline_shopping_info.to_alipay_dict()
            else:
                params['offline_shopping_info'] = self.offline_shopping_info
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.parent_order_id:
            if hasattr(self.parent_order_id, 'to_alipay_dict'):
                params['parent_order_id'] = self.parent_order_id.to_alipay_dict()
            else:
                params['parent_order_id'] = self.parent_order_id
        if self.path_info:
            if hasattr(self.path_info, 'to_alipay_dict'):
                params['path_info'] = self.path_info.to_alipay_dict()
            else:
                params['path_info'] = self.path_info
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.relet_info:
            if hasattr(self.relet_info, 'to_alipay_dict'):
                params['relet_info'] = self.relet_info.to_alipay_dict()
            else:
                params['relet_info'] = self.relet_info
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
        if self.service_provider_model:
            if hasattr(self.service_provider_model, 'to_alipay_dict'):
                params['service_provider_model'] = self.service_provider_model.to_alipay_dict()
            else:
                params['service_provider_model'] = self.service_provider_model
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
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
        if self.zst_info:
            if hasattr(self.zst_info, 'to_alipay_dict'):
                params['zst_info'] = self.zst_info.to_alipay_dict()
            else:
                params['zst_info'] = self.zst_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderCreateModel()
        if 'activity_consult_id' in d:
            o.activity_consult_id = d['activity_consult_id']
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'buyout_info' in d:
            o.buyout_info = d['buyout_info']
        if 'buyout_installment_no' in d:
            o.buyout_installment_no = d['buyout_installment_no']
        if 'default_receiving_address' in d:
            o.default_receiving_address = d['default_receiving_address']
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'memo' in d:
            o.memo = d['memo']
        if 'offline_shopping_info' in d:
            o.offline_shopping_info = d['offline_shopping_info']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'parent_order_id' in d:
            o.parent_order_id = d['parent_order_id']
        if 'path_info' in d:
            o.path_info = d['path_info']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'relet_info' in d:
            o.relet_info = d['relet_info']
        if 'rent_plan_info' in d:
            o.rent_plan_info = d['rent_plan_info']
        if 'rent_sign_info' in d:
            o.rent_sign_info = d['rent_sign_info']
        if 'service_provider_model' in d:
            o.service_provider_model = d['service_provider_model']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'title' in d:
            o.title = d['title']
        if 'trade_app_id' in d:
            o.trade_app_id = d['trade_app_id']
        if 'zst_info' in d:
            o.zst_info = d['zst_info']
        return o


