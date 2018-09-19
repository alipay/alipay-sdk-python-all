#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbOrderActivityModel import KbOrderActivityModel
from alipay.aop.api.domain.KbOrderFundsVoucherModel import KbOrderFundsVoucherModel
from alipay.aop.api.domain.KbOrderShopModel import KbOrderShopModel
from alipay.aop.api.domain.KbOrderVoucherModel import KbOrderVoucherModel


class KoubeiTradeOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeOrderQueryResponse, self).__init__()
        self._activity_infos = None
        self._buyer_id = None
        self._contact = None
        self._funds_vouchers = None
        self._gmt_create = None
        self._gmt_modified = None
        self._order_no = None
        self._out_biz_no = None
        self._partner_id = None
        self._real_amount = None
        self._seller_id = None
        self._shop = None
        self._status = None
        self._total_amount = None
        self._trans_no = None
        self._vouchers = None

    @property
    def activity_infos(self):
        return self._activity_infos

    @activity_infos.setter
    def activity_infos(self, value):
        if isinstance(value, list):
            self._activity_infos = list()
            for i in value:
                if isinstance(i, KbOrderActivityModel):
                    self._activity_infos.append(i)
                else:
                    self._activity_infos.append(KbOrderActivityModel.from_alipay_dict(i))
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
    @property
    def funds_vouchers(self):
        return self._funds_vouchers

    @funds_vouchers.setter
    def funds_vouchers(self, value):
        if isinstance(value, list):
            self._funds_vouchers = list()
            for i in value:
                if isinstance(i, KbOrderFundsVoucherModel):
                    self._funds_vouchers.append(i)
                else:
                    self._funds_vouchers.append(KbOrderFundsVoucherModel.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def shop(self):
        return self._shop

    @shop.setter
    def shop(self, value):
        if isinstance(value, KbOrderShopModel):
            self._shop = value
        else:
            self._shop = KbOrderShopModel.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trans_no(self):
        return self._trans_no

    @trans_no.setter
    def trans_no(self, value):
        self._trans_no = value
    @property
    def vouchers(self):
        return self._vouchers

    @vouchers.setter
    def vouchers(self, value):
        if isinstance(value, list):
            self._vouchers = list()
            for i in value:
                if isinstance(i, KbOrderVoucherModel):
                    self._vouchers.append(i)
                else:
                    self._vouchers.append(KbOrderVoucherModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeOrderQueryResponse, self).parse_response_content(response_content)
        if 'activity_infos' in response:
            self.activity_infos = response['activity_infos']
        if 'buyer_id' in response:
            self.buyer_id = response['buyer_id']
        if 'contact' in response:
            self.contact = response['contact']
        if 'funds_vouchers' in response:
            self.funds_vouchers = response['funds_vouchers']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'real_amount' in response:
            self.real_amount = response['real_amount']
        if 'seller_id' in response:
            self.seller_id = response['seller_id']
        if 'shop' in response:
            self.shop = response['shop']
        if 'status' in response:
            self.status = response['status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trans_no' in response:
            self.trans_no = response['trans_no']
        if 'vouchers' in response:
            self.vouchers = response['vouchers']
