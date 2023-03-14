#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BkAgentReqInfoDTO import BkAgentReqInfoDTO
from alipay.aop.api.domain.BusinessParamsDTO import BusinessParamsDTO
from alipay.aop.api.domain.OrderExtInfoDTO import OrderExtInfoDTO
from alipay.aop.api.domain.ExtUserInfoDTO import ExtUserInfoDTO
from alipay.aop.api.domain.ExtendParamsDTO import ExtendParamsDTO
from alipay.aop.api.domain.GoodsDetailInfoDTO import GoodsDetailInfoDTO
from alipay.aop.api.domain.LogisticsDetailDTO import LogisticsDetailDTO
from alipay.aop.api.domain.ReceiverAddressInfoDTO import ReceiverAddressInfoDTO
from alipay.aop.api.domain.RoyaltyInfoDTO import RoyaltyInfoDTO
from alipay.aop.api.domain.SettleInfoDTO import SettleInfoDTO
from alipay.aop.api.domain.SubMerchantDTO import SubMerchantDTO


class AlipayOpenMiniTradeCreateModel(object):

    def __init__(self):
        self._bkagent_req_info = None
        self._body = None
        self._business_params = None
        self._buyer_id = None
        self._buyer_logon_id = None
        self._buyer_open_id = None
        self._discountable_amount = None
        self._ext_info = None
        self._ext_user_info = None
        self._extend_params = None
        self._item_order_list = None
        self._logistics_info = None
        self._merchant_biz_type = None
        self._merchant_order_link_page = None
        self._operator_id = None
        self._out_trade_no = None
        self._query_options = None
        self._receiver_address_info = None
        self._royalty_info = None
        self._seller_id = None
        self._seller_open_id = None
        self._settle_info = None
        self._store_id = None
        self._sub_merchant = None
        self._subject = None
        self._terminal_id = None
        self._time_expire = None
        self._timeout_express = None
        self._total_amount = None
        self._undiscountable_amount = None

    @property
    def bkagent_req_info(self):
        return self._bkagent_req_info

    @bkagent_req_info.setter
    def bkagent_req_info(self, value):
        if isinstance(value, BkAgentReqInfoDTO):
            self._bkagent_req_info = value
        else:
            self._bkagent_req_info = BkAgentReqInfoDTO.from_alipay_dict(value)
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, BusinessParamsDTO):
            self._business_params = value
        else:
            self._business_params = BusinessParamsDTO.from_alipay_dict(value)
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
    def discountable_amount(self):
        return self._discountable_amount

    @discountable_amount.setter
    def discountable_amount(self, value):
        self._discountable_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, OrderExtInfoDTO):
            self._ext_info = value
        else:
            self._ext_info = OrderExtInfoDTO.from_alipay_dict(value)
    @property
    def ext_user_info(self):
        return self._ext_user_info

    @ext_user_info.setter
    def ext_user_info(self, value):
        if isinstance(value, ExtUserInfoDTO):
            self._ext_user_info = value
        else:
            self._ext_user_info = ExtUserInfoDTO.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ExtendParamsDTO):
            self._extend_params = value
        else:
            self._extend_params = ExtendParamsDTO.from_alipay_dict(value)
    @property
    def item_order_list(self):
        return self._item_order_list

    @item_order_list.setter
    def item_order_list(self, value):
        if isinstance(value, list):
            self._item_order_list = list()
            for i in value:
                if isinstance(i, GoodsDetailInfoDTO):
                    self._item_order_list.append(i)
                else:
                    self._item_order_list.append(GoodsDetailInfoDTO.from_alipay_dict(i))
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, LogisticsDetailDTO):
            self._logistics_info = value
        else:
            self._logistics_info = LogisticsDetailDTO.from_alipay_dict(value)
    @property
    def merchant_biz_type(self):
        return self._merchant_biz_type

    @merchant_biz_type.setter
    def merchant_biz_type(self, value):
        self._merchant_biz_type = value
    @property
    def merchant_order_link_page(self):
        return self._merchant_order_link_page

    @merchant_order_link_page.setter
    def merchant_order_link_page(self, value):
        self._merchant_order_link_page = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def query_options(self):
        return self._query_options

    @query_options.setter
    def query_options(self, value):
        if isinstance(value, list):
            self._query_options = list()
            for i in value:
                self._query_options.append(i)
    @property
    def receiver_address_info(self):
        return self._receiver_address_info

    @receiver_address_info.setter
    def receiver_address_info(self, value):
        if isinstance(value, ReceiverAddressInfoDTO):
            self._receiver_address_info = value
        else:
            self._receiver_address_info = ReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def royalty_info(self):
        return self._royalty_info

    @royalty_info.setter
    def royalty_info(self, value):
        if isinstance(value, RoyaltyInfoDTO):
            self._royalty_info = value
        else:
            self._royalty_info = RoyaltyInfoDTO.from_alipay_dict(value)
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_open_id(self):
        return self._seller_open_id

    @seller_open_id.setter
    def seller_open_id(self, value):
        self._seller_open_id = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, SettleInfoDTO):
            self._settle_info = value
        else:
            self._settle_info = SettleInfoDTO.from_alipay_dict(value)
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
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
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def undiscountable_amount(self):
        return self._undiscountable_amount

    @undiscountable_amount.setter
    def undiscountable_amount(self, value):
        self._undiscountable_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bkagent_req_info:
            if hasattr(self.bkagent_req_info, 'to_alipay_dict'):
                params['bkagent_req_info'] = self.bkagent_req_info.to_alipay_dict()
            else:
                params['bkagent_req_info'] = self.bkagent_req_info
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
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
        if self.discountable_amount:
            if hasattr(self.discountable_amount, 'to_alipay_dict'):
                params['discountable_amount'] = self.discountable_amount.to_alipay_dict()
            else:
                params['discountable_amount'] = self.discountable_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.ext_user_info:
            if hasattr(self.ext_user_info, 'to_alipay_dict'):
                params['ext_user_info'] = self.ext_user_info.to_alipay_dict()
            else:
                params['ext_user_info'] = self.ext_user_info
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.item_order_list:
            if isinstance(self.item_order_list, list):
                for i in range(0, len(self.item_order_list)):
                    element = self.item_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_order_list[i] = element.to_alipay_dict()
            if hasattr(self.item_order_list, 'to_alipay_dict'):
                params['item_order_list'] = self.item_order_list.to_alipay_dict()
            else:
                params['item_order_list'] = self.item_order_list
        if self.logistics_info:
            if hasattr(self.logistics_info, 'to_alipay_dict'):
                params['logistics_info'] = self.logistics_info.to_alipay_dict()
            else:
                params['logistics_info'] = self.logistics_info
        if self.merchant_biz_type:
            if hasattr(self.merchant_biz_type, 'to_alipay_dict'):
                params['merchant_biz_type'] = self.merchant_biz_type.to_alipay_dict()
            else:
                params['merchant_biz_type'] = self.merchant_biz_type
        if self.merchant_order_link_page:
            if hasattr(self.merchant_order_link_page, 'to_alipay_dict'):
                params['merchant_order_link_page'] = self.merchant_order_link_page.to_alipay_dict()
            else:
                params['merchant_order_link_page'] = self.merchant_order_link_page
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.query_options:
            if isinstance(self.query_options, list):
                for i in range(0, len(self.query_options)):
                    element = self.query_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_options[i] = element.to_alipay_dict()
            if hasattr(self.query_options, 'to_alipay_dict'):
                params['query_options'] = self.query_options.to_alipay_dict()
            else:
                params['query_options'] = self.query_options
        if self.receiver_address_info:
            if hasattr(self.receiver_address_info, 'to_alipay_dict'):
                params['receiver_address_info'] = self.receiver_address_info.to_alipay_dict()
            else:
                params['receiver_address_info'] = self.receiver_address_info
        if self.royalty_info:
            if hasattr(self.royalty_info, 'to_alipay_dict'):
                params['royalty_info'] = self.royalty_info.to_alipay_dict()
            else:
                params['royalty_info'] = self.royalty_info
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_open_id:
            if hasattr(self.seller_open_id, 'to_alipay_dict'):
                params['seller_open_id'] = self.seller_open_id.to_alipay_dict()
            else:
                params['seller_open_id'] = self.seller_open_id
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.undiscountable_amount:
            if hasattr(self.undiscountable_amount, 'to_alipay_dict'):
                params['undiscountable_amount'] = self.undiscountable_amount.to_alipay_dict()
            else:
                params['undiscountable_amount'] = self.undiscountable_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniTradeCreateModel()
        if 'bkagent_req_info' in d:
            o.bkagent_req_info = d['bkagent_req_info']
        if 'body' in d:
            o.body = d['body']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_logon_id' in d:
            o.buyer_logon_id = d['buyer_logon_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'discountable_amount' in d:
            o.discountable_amount = d['discountable_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ext_user_info' in d:
            o.ext_user_info = d['ext_user_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'item_order_list' in d:
            o.item_order_list = d['item_order_list']
        if 'logistics_info' in d:
            o.logistics_info = d['logistics_info']
        if 'merchant_biz_type' in d:
            o.merchant_biz_type = d['merchant_biz_type']
        if 'merchant_order_link_page' in d:
            o.merchant_order_link_page = d['merchant_order_link_page']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'query_options' in d:
            o.query_options = d['query_options']
        if 'receiver_address_info' in d:
            o.receiver_address_info = d['receiver_address_info']
        if 'royalty_info' in d:
            o.royalty_info = d['royalty_info']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_open_id' in d:
            o.seller_open_id = d['seller_open_id']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'subject' in d:
            o.subject = d['subject']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'undiscountable_amount' in d:
            o.undiscountable_amount = d['undiscountable_amount']
        return o


