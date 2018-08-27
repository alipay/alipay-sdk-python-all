#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MaintainBizOrderExpress import MaintainBizOrderExpress
from alipay.aop.api.domain.MaintainBizOrderGoods import MaintainBizOrderGoods
from alipay.aop.api.domain.MaintainBizOrderServer import MaintainBizOrderServer


class AlipayEcoMycarMaintainBizorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarMaintainBizorderQueryResponse, self).__init__()
        self._appoint_affirm_time = None
        self._appoint_end_time = None
        self._appoint_start_time = None
        self._appoint_status = None
        self._arrive_time = None
        self._biz_status_txt = None
        self._biz_type = None
        self._car_id = None
        self._create_time = None
        self._order_express_list = None
        self._order_goods_list = None
        self._order_no = None
        self._order_server_list = None
        self._order_status = None
        self._original_cost = None
        self._out_order_no = None
        self._out_shop_id = None
        self._pay_time = None
        self._real_cost = None
        self._shop_id = None
        self._shop_name = None
        self._update_time = None
        self._user_id = None

    @property
    def appoint_affirm_time(self):
        return self._appoint_affirm_time

    @appoint_affirm_time.setter
    def appoint_affirm_time(self, value):
        self._appoint_affirm_time = value
    @property
    def appoint_end_time(self):
        return self._appoint_end_time

    @appoint_end_time.setter
    def appoint_end_time(self, value):
        self._appoint_end_time = value
    @property
    def appoint_start_time(self):
        return self._appoint_start_time

    @appoint_start_time.setter
    def appoint_start_time(self, value):
        self._appoint_start_time = value
    @property
    def appoint_status(self):
        return self._appoint_status

    @appoint_status.setter
    def appoint_status(self, value):
        self._appoint_status = value
    @property
    def arrive_time(self):
        return self._arrive_time

    @arrive_time.setter
    def arrive_time(self, value):
        self._arrive_time = value
    @property
    def biz_status_txt(self):
        return self._biz_status_txt

    @biz_status_txt.setter
    def biz_status_txt(self, value):
        self._biz_status_txt = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, value):
        self._car_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def order_express_list(self):
        return self._order_express_list

    @order_express_list.setter
    def order_express_list(self, value):
        if isinstance(value, list):
            self._order_express_list = list()
            for i in value:
                if isinstance(i, MaintainBizOrderExpress):
                    self._order_express_list.append(i)
                else:
                    self._order_express_list.append(MaintainBizOrderExpress.from_alipay_dict(i))
    @property
    def order_goods_list(self):
        return self._order_goods_list

    @order_goods_list.setter
    def order_goods_list(self, value):
        if isinstance(value, list):
            self._order_goods_list = list()
            for i in value:
                if isinstance(i, MaintainBizOrderGoods):
                    self._order_goods_list.append(i)
                else:
                    self._order_goods_list.append(MaintainBizOrderGoods.from_alipay_dict(i))
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_server_list(self):
        return self._order_server_list

    @order_server_list.setter
    def order_server_list(self, value):
        if isinstance(value, list):
            self._order_server_list = list()
            for i in value:
                if isinstance(i, MaintainBizOrderServer):
                    self._order_server_list.append(i)
                else:
                    self._order_server_list.append(MaintainBizOrderServer.from_alipay_dict(i))
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def original_cost(self):
        return self._original_cost

    @original_cost.setter
    def original_cost(self, value):
        self._original_cost = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def real_cost(self):
        return self._real_cost

    @real_cost.setter
    def real_cost(self, value):
        self._real_cost = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarMaintainBizorderQueryResponse, self).parse_response_content(response_content)
        if 'appoint_affirm_time' in response:
            self.appoint_affirm_time = response['appoint_affirm_time']
        if 'appoint_end_time' in response:
            self.appoint_end_time = response['appoint_end_time']
        if 'appoint_start_time' in response:
            self.appoint_start_time = response['appoint_start_time']
        if 'appoint_status' in response:
            self.appoint_status = response['appoint_status']
        if 'arrive_time' in response:
            self.arrive_time = response['arrive_time']
        if 'biz_status_txt' in response:
            self.biz_status_txt = response['biz_status_txt']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'car_id' in response:
            self.car_id = response['car_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'order_express_list' in response:
            self.order_express_list = response['order_express_list']
        if 'order_goods_list' in response:
            self.order_goods_list = response['order_goods_list']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_server_list' in response:
            self.order_server_list = response['order_server_list']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'original_cost' in response:
            self.original_cost = response['original_cost']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_shop_id' in response:
            self.out_shop_id = response['out_shop_id']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'real_cost' in response:
            self.real_cost = response['real_cost']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_name' in response:
            self.shop_name = response['shop_name']
        if 'update_time' in response:
            self.update_time = response['update_time']
        if 'user_id' in response:
            self.user_id = response['user_id']
