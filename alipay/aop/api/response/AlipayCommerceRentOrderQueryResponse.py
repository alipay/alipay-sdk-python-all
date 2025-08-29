#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentOrderReceiverAddressInfoVO import RentOrderReceiverAddressInfoVO
from alipay.aop.api.domain.RentOrderReceiverAddressInfoVO import RentOrderReceiverAddressInfoVO
from alipay.aop.api.domain.RentOrderDeliveryInfoVO import RentOrderDeliveryInfoVO
from alipay.aop.api.domain.RentOrderExtendInfoVO import RentOrderExtendInfoVO
from alipay.aop.api.domain.RentFastAuditInfoVO import RentFastAuditInfoVO
from alipay.aop.api.domain.RentGoodsDetailInfoVO import RentGoodsDetailInfoVO
from alipay.aop.api.domain.RentPathInfoVO import RentPathInfoVO
from alipay.aop.api.domain.RentOrderPriceInfoVO import RentOrderPriceInfoVO
from alipay.aop.api.domain.RentPromoInfoVO import RentPromoInfoVO
from alipay.aop.api.domain.RentAftersaleOrderVO import RentAftersaleOrderVO
from alipay.aop.api.domain.RentOrderPayInfoVO import RentOrderPayInfoVO
from alipay.aop.api.domain.RentPlanInfoVO import RentPlanInfoVO
from alipay.aop.api.domain.RentSignInfoVO import RentSignInfoVO
from alipay.aop.api.domain.RentOrderStatementInfoVO import RentOrderStatementInfoVO
from alipay.aop.api.domain.RentSubMerchantVO import RentSubMerchantVO
from alipay.aop.api.domain.RentFulfillmentDeliveryInfoVO import RentFulfillmentDeliveryInfoVO


class AlipayCommerceRentOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderQueryResponse, self).__init__()
        self._address_info = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._default_receiving_address = None
        self._delivery_info = None
        self._extend_info = None
        self._face_verify_result = None
        self._fast_audit_info = None
        self._item_infos = None
        self._memo = None
        self._order_create_time = None
        self._order_id = None
        self._order_type = None
        self._out_order_id = None
        self._path_info = None
        self._price_info = None
        self._promo_info = None
        self._rent_aftersale_orders = None
        self._rent_pay_infos = None
        self._rent_plan_info = None
        self._rent_sign_info = None
        self._rent_statement_infos = None
        self._settle_type = None
        self._status = None
        self._sub_merchant = None
        self._sub_order_ids = None
        self._title = None
        self._trade_app_id = None
        self._user_delivery_logistics_infos = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RentOrderReceiverAddressInfoVO):
            self._address_info = value
        else:
            self._address_info = RentOrderReceiverAddressInfoVO.from_alipay_dict(value)
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
    def default_receiving_address(self):
        return self._default_receiving_address

    @default_receiving_address.setter
    def default_receiving_address(self, value):
        if isinstance(value, RentOrderReceiverAddressInfoVO):
            self._default_receiving_address = value
        else:
            self._default_receiving_address = RentOrderReceiverAddressInfoVO.from_alipay_dict(value)
    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, RentOrderDeliveryInfoVO):
            self._delivery_info = value
        else:
            self._delivery_info = RentOrderDeliveryInfoVO.from_alipay_dict(value)
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        if isinstance(value, RentOrderExtendInfoVO):
            self._extend_info = value
        else:
            self._extend_info = RentOrderExtendInfoVO.from_alipay_dict(value)
    @property
    def face_verify_result(self):
        return self._face_verify_result

    @face_verify_result.setter
    def face_verify_result(self, value):
        self._face_verify_result = value
    @property
    def fast_audit_info(self):
        return self._fast_audit_info

    @fast_audit_info.setter
    def fast_audit_info(self, value):
        if isinstance(value, RentFastAuditInfoVO):
            self._fast_audit_info = value
        else:
            self._fast_audit_info = RentFastAuditInfoVO.from_alipay_dict(value)
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, RentGoodsDetailInfoVO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(RentGoodsDetailInfoVO.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
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
    def path_info(self):
        return self._path_info

    @path_info.setter
    def path_info(self, value):
        if isinstance(value, RentPathInfoVO):
            self._path_info = value
        else:
            self._path_info = RentPathInfoVO.from_alipay_dict(value)
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, RentOrderPriceInfoVO):
            self._price_info = value
        else:
            self._price_info = RentOrderPriceInfoVO.from_alipay_dict(value)
    @property
    def promo_info(self):
        return self._promo_info

    @promo_info.setter
    def promo_info(self, value):
        if isinstance(value, RentPromoInfoVO):
            self._promo_info = value
        else:
            self._promo_info = RentPromoInfoVO.from_alipay_dict(value)
    @property
    def rent_aftersale_orders(self):
        return self._rent_aftersale_orders

    @rent_aftersale_orders.setter
    def rent_aftersale_orders(self, value):
        if isinstance(value, list):
            self._rent_aftersale_orders = list()
            for i in value:
                if isinstance(i, RentAftersaleOrderVO):
                    self._rent_aftersale_orders.append(i)
                else:
                    self._rent_aftersale_orders.append(RentAftersaleOrderVO.from_alipay_dict(i))
    @property
    def rent_pay_infos(self):
        return self._rent_pay_infos

    @rent_pay_infos.setter
    def rent_pay_infos(self, value):
        if isinstance(value, list):
            self._rent_pay_infos = list()
            for i in value:
                if isinstance(i, RentOrderPayInfoVO):
                    self._rent_pay_infos.append(i)
                else:
                    self._rent_pay_infos.append(RentOrderPayInfoVO.from_alipay_dict(i))
    @property
    def rent_plan_info(self):
        return self._rent_plan_info

    @rent_plan_info.setter
    def rent_plan_info(self, value):
        if isinstance(value, RentPlanInfoVO):
            self._rent_plan_info = value
        else:
            self._rent_plan_info = RentPlanInfoVO.from_alipay_dict(value)
    @property
    def rent_sign_info(self):
        return self._rent_sign_info

    @rent_sign_info.setter
    def rent_sign_info(self, value):
        if isinstance(value, RentSignInfoVO):
            self._rent_sign_info = value
        else:
            self._rent_sign_info = RentSignInfoVO.from_alipay_dict(value)
    @property
    def rent_statement_infos(self):
        return self._rent_statement_infos

    @rent_statement_infos.setter
    def rent_statement_infos(self, value):
        if isinstance(value, list):
            self._rent_statement_infos = list()
            for i in value:
                if isinstance(i, RentOrderStatementInfoVO):
                    self._rent_statement_infos.append(i)
                else:
                    self._rent_statement_infos.append(RentOrderStatementInfoVO.from_alipay_dict(i))
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, RentSubMerchantVO):
            self._sub_merchant = value
        else:
            self._sub_merchant = RentSubMerchantVO.from_alipay_dict(value)
    @property
    def sub_order_ids(self):
        return self._sub_order_ids

    @sub_order_ids.setter
    def sub_order_ids(self, value):
        if isinstance(value, list):
            self._sub_order_ids = list()
            for i in value:
                self._sub_order_ids.append(i)
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
    def user_delivery_logistics_infos(self):
        return self._user_delivery_logistics_infos

    @user_delivery_logistics_infos.setter
    def user_delivery_logistics_infos(self, value):
        if isinstance(value, list):
            self._user_delivery_logistics_infos = list()
            for i in value:
                if isinstance(i, RentFulfillmentDeliveryInfoVO):
                    self._user_delivery_logistics_infos.append(i)
                else:
                    self._user_delivery_logistics_infos.append(RentFulfillmentDeliveryInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderQueryResponse, self).parse_response_content(response_content)
        if 'address_info' in response:
            self.address_info = response['address_info']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'buyer_open_id' in response:
            self.buyer_open_id = response['buyer_open_id']
        if 'default_receiving_address' in response:
            self.default_receiving_address = response['default_receiving_address']
        if 'delivery_info' in response:
            self.delivery_info = response['delivery_info']
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'face_verify_result' in response:
            self.face_verify_result = response['face_verify_result']
        if 'fast_audit_info' in response:
            self.fast_audit_info = response['fast_audit_info']
        if 'item_infos' in response:
            self.item_infos = response['item_infos']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_create_time' in response:
            self.order_create_time = response['order_create_time']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'path_info' in response:
            self.path_info = response['path_info']
        if 'price_info' in response:
            self.price_info = response['price_info']
        if 'promo_info' in response:
            self.promo_info = response['promo_info']
        if 'rent_aftersale_orders' in response:
            self.rent_aftersale_orders = response['rent_aftersale_orders']
        if 'rent_pay_infos' in response:
            self.rent_pay_infos = response['rent_pay_infos']
        if 'rent_plan_info' in response:
            self.rent_plan_info = response['rent_plan_info']
        if 'rent_sign_info' in response:
            self.rent_sign_info = response['rent_sign_info']
        if 'rent_statement_infos' in response:
            self.rent_statement_infos = response['rent_statement_infos']
        if 'settle_type' in response:
            self.settle_type = response['settle_type']
        if 'status' in response:
            self.status = response['status']
        if 'sub_merchant' in response:
            self.sub_merchant = response['sub_merchant']
        if 'sub_order_ids' in response:
            self.sub_order_ids = response['sub_order_ids']
        if 'title' in response:
            self.title = response['title']
        if 'trade_app_id' in response:
            self.trade_app_id = response['trade_app_id']
        if 'user_delivery_logistics_infos' in response:
            self.user_delivery_logistics_infos = response['user_delivery_logistics_infos']
