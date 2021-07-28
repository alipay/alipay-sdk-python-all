#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PriceInformation import PriceInformation
from alipay.aop.api.domain.BizUnitInfo import BizUnitInfo
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.PriceInformation import PriceInformation
from alipay.aop.api.domain.UserIdentity import UserIdentity


class AlipayMerchantOrderMessageSyncModel(object):

    def __init__(self):
        self._actual_amount = None
        self._alipay_trade_no = None
        self._biz_order_no = None
        self._biz_type = None
        self._biz_unit_info = None
        self._buyer = None
        self._callback_url = None
        self._create_time = None
        self._deliver_status = None
        self._deliver_status_desc = None
        self._ext_info = None
        self._external_buyer = None
        self._external_order_no = None
        self._external_seller = None
        self._item_title = None
        self._modify_time = None
        self._order_amount = None
        self._order_status = None
        self._order_status_desc = None
        self._partner_id = None
        self._pay_status = None
        self._pay_status_desc = None
        self._pay_time = None
        self._refund_status = None
        self._refund_status_desc = None
        self._seller = None
        self._source = None
        self._sub_biz_type = None
        self._system_name = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        if isinstance(value, list):
            self._actual_amount = list()
            for i in value:
                if isinstance(i, PriceInformation):
                    self._actual_amount.append(i)
                else:
                    self._actual_amount.append(PriceInformation.from_alipay_dict(i))
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def biz_unit_info(self):
        return self._biz_unit_info

    @biz_unit_info.setter
    def biz_unit_info(self, value):
        if isinstance(value, BizUnitInfo):
            self._biz_unit_info = value
        else:
            self._biz_unit_info = BizUnitInfo.from_alipay_dict(value)
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, UserIdentity):
            self._buyer = value
        else:
            self._buyer = UserIdentity.from_alipay_dict(value)
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def deliver_status(self):
        return self._deliver_status

    @deliver_status.setter
    def deliver_status(self, value):
        self._deliver_status = value
    @property
    def deliver_status_desc(self):
        return self._deliver_status_desc

    @deliver_status_desc.setter
    def deliver_status_desc(self, value):
        self._deliver_status_desc = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def external_buyer(self):
        return self._external_buyer

    @external_buyer.setter
    def external_buyer(self, value):
        if isinstance(value, UserIdentity):
            self._external_buyer = value
        else:
            self._external_buyer = UserIdentity.from_alipay_dict(value)
    @property
    def external_order_no(self):
        return self._external_order_no

    @external_order_no.setter
    def external_order_no(self, value):
        self._external_order_no = value
    @property
    def external_seller(self):
        return self._external_seller

    @external_seller.setter
    def external_seller(self, value):
        if isinstance(value, UserIdentity):
            self._external_seller = value
        else:
            self._external_seller = UserIdentity.from_alipay_dict(value)
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        if isinstance(value, list):
            self._order_amount = list()
            for i in value:
                if isinstance(i, PriceInformation):
                    self._order_amount.append(i)
                else:
                    self._order_amount.append(PriceInformation.from_alipay_dict(i))
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_status_desc(self):
        return self._order_status_desc

    @order_status_desc.setter
    def order_status_desc(self, value):
        self._order_status_desc = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_status_desc(self):
        return self._pay_status_desc

    @pay_status_desc.setter
    def pay_status_desc(self, value):
        self._pay_status_desc = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_status_desc(self):
        return self._refund_status_desc

    @refund_status_desc.setter
    def refund_status_desc(self, value):
        self._refund_status_desc = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, UserIdentity):
            self._seller = value
        else:
            self._seller = UserIdentity.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def system_name(self):
        return self._system_name

    @system_name.setter
    def system_name(self, value):
        self._system_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if isinstance(self.actual_amount, list):
                for i in range(0, len(self.actual_amount)):
                    element = self.actual_amount[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.actual_amount[i] = element.to_alipay_dict()
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.biz_order_no:
            if hasattr(self.biz_order_no, 'to_alipay_dict'):
                params['biz_order_no'] = self.biz_order_no.to_alipay_dict()
            else:
                params['biz_order_no'] = self.biz_order_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.biz_unit_info:
            if hasattr(self.biz_unit_info, 'to_alipay_dict'):
                params['biz_unit_info'] = self.biz_unit_info.to_alipay_dict()
            else:
                params['biz_unit_info'] = self.biz_unit_info
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.deliver_status:
            if hasattr(self.deliver_status, 'to_alipay_dict'):
                params['deliver_status'] = self.deliver_status.to_alipay_dict()
            else:
                params['deliver_status'] = self.deliver_status
        if self.deliver_status_desc:
            if hasattr(self.deliver_status_desc, 'to_alipay_dict'):
                params['deliver_status_desc'] = self.deliver_status_desc.to_alipay_dict()
            else:
                params['deliver_status_desc'] = self.deliver_status_desc
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_buyer:
            if hasattr(self.external_buyer, 'to_alipay_dict'):
                params['external_buyer'] = self.external_buyer.to_alipay_dict()
            else:
                params['external_buyer'] = self.external_buyer
        if self.external_order_no:
            if hasattr(self.external_order_no, 'to_alipay_dict'):
                params['external_order_no'] = self.external_order_no.to_alipay_dict()
            else:
                params['external_order_no'] = self.external_order_no
        if self.external_seller:
            if hasattr(self.external_seller, 'to_alipay_dict'):
                params['external_seller'] = self.external_seller.to_alipay_dict()
            else:
                params['external_seller'] = self.external_seller
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.order_amount:
            if isinstance(self.order_amount, list):
                for i in range(0, len(self.order_amount)):
                    element = self.order_amount[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_amount[i] = element.to_alipay_dict()
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_status_desc:
            if hasattr(self.order_status_desc, 'to_alipay_dict'):
                params['order_status_desc'] = self.order_status_desc.to_alipay_dict()
            else:
                params['order_status_desc'] = self.order_status_desc
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.pay_status_desc:
            if hasattr(self.pay_status_desc, 'to_alipay_dict'):
                params['pay_status_desc'] = self.pay_status_desc.to_alipay_dict()
            else:
                params['pay_status_desc'] = self.pay_status_desc
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.refund_status_desc:
            if hasattr(self.refund_status_desc, 'to_alipay_dict'):
                params['refund_status_desc'] = self.refund_status_desc.to_alipay_dict()
            else:
                params['refund_status_desc'] = self.refund_status_desc
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.system_name:
            if hasattr(self.system_name, 'to_alipay_dict'):
                params['system_name'] = self.system_name.to_alipay_dict()
            else:
                params['system_name'] = self.system_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderMessageSyncModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'biz_order_no' in d:
            o.biz_order_no = d['biz_order_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'biz_unit_info' in d:
            o.biz_unit_info = d['biz_unit_info']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'deliver_status' in d:
            o.deliver_status = d['deliver_status']
        if 'deliver_status_desc' in d:
            o.deliver_status_desc = d['deliver_status_desc']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_buyer' in d:
            o.external_buyer = d['external_buyer']
        if 'external_order_no' in d:
            o.external_order_no = d['external_order_no']
        if 'external_seller' in d:
            o.external_seller = d['external_seller']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_status_desc' in d:
            o.order_status_desc = d['order_status_desc']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'pay_status_desc' in d:
            o.pay_status_desc = d['pay_status_desc']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'refund_status_desc' in d:
            o.refund_status_desc = d['refund_status_desc']
        if 'seller' in d:
            o.seller = d['seller']
        if 'source' in d:
            o.source = d['source']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'system_name' in d:
            o.system_name = d['system_name']
        return o


