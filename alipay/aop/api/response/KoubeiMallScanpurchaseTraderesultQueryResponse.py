#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MallConsumeVoucher import MallConsumeVoucher
from alipay.aop.api.domain.MallGoodsDetail import MallGoodsDetail
from alipay.aop.api.domain.SceneOrder import SceneOrder
from alipay.aop.api.domain.MallUserVerify import MallUserVerify


class KoubeiMallScanpurchaseTraderesultQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMallScanpurchaseTraderesultQueryResponse, self).__init__()
        self._banner = None
        self._buyer_user_id = None
        self._consume_voucher = None
        self._goods_details = None
        self._out_trade_no = None
        self._scene_order = None
        self._seller_user_id = None
        self._trade_no = None
        self._user_verify = None

    @property
    def banner(self):
        return self._banner

    @banner.setter
    def banner(self, value):
        self._banner = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def consume_voucher(self):
        return self._consume_voucher

    @consume_voucher.setter
    def consume_voucher(self, value):
        if isinstance(value, MallConsumeVoucher):
            self._consume_voucher = value
        else:
            self._consume_voucher = MallConsumeVoucher.from_alipay_dict(value)
    @property
    def goods_details(self):
        return self._goods_details

    @goods_details.setter
    def goods_details(self, value):
        if isinstance(value, list):
            self._goods_details = list()
            for i in value:
                if isinstance(i, MallGoodsDetail):
                    self._goods_details.append(i)
                else:
                    self._goods_details.append(MallGoodsDetail.from_alipay_dict(i))
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def scene_order(self):
        return self._scene_order

    @scene_order.setter
    def scene_order(self, value):
        if isinstance(value, SceneOrder):
            self._scene_order = value
        else:
            self._scene_order = SceneOrder.from_alipay_dict(value)
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_verify(self):
        return self._user_verify

    @user_verify.setter
    def user_verify(self, value):
        if isinstance(value, MallUserVerify):
            self._user_verify = value
        else:
            self._user_verify = MallUserVerify.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMallScanpurchaseTraderesultQueryResponse, self).parse_response_content(response_content)
        if 'banner' in response:
            self.banner = response['banner']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'consume_voucher' in response:
            self.consume_voucher = response['consume_voucher']
        if 'goods_details' in response:
            self.goods_details = response['goods_details']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'scene_order' in response:
            self.scene_order = response['scene_order']
        if 'seller_user_id' in response:
            self.seller_user_id = response['seller_user_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'user_verify' in response:
            self.user_verify = response['user_verify']
