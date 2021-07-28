#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsDetail import GoodsDetail


class AlipayPayAppMarketingConsultModel(object):

    def __init__(self):
        self._biz_scene = None
        self._blind_mobile = None
        self._confused_mobile_list = None
        self._device_id = None
        self._device_type = None
        self._encrypted_mobile = None
        self._goods_detail = None
        self._mobile = None
        self._need_query_anti_rank = None
        self._need_query_marketing_rank = None
        self._need_return_tag = None
        self._out_trade_no = None
        self._product_code = None
        self._promo_params = None
        self._seller_id = None
        self._total_amount = None
        self._undiscountable_amount = None
        self._user_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def blind_mobile(self):
        return self._blind_mobile

    @blind_mobile.setter
    def blind_mobile(self, value):
        self._blind_mobile = value
    @property
    def confused_mobile_list(self):
        return self._confused_mobile_list

    @confused_mobile_list.setter
    def confused_mobile_list(self, value):
        if isinstance(value, list):
            self._confused_mobile_list = list()
            for i in value:
                self._confused_mobile_list.append(i)
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def encrypted_mobile(self):
        return self._encrypted_mobile

    @encrypted_mobile.setter
    def encrypted_mobile(self, value):
        self._encrypted_mobile = value
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, list):
            self._goods_detail = list()
            for i in value:
                if isinstance(i, GoodsDetail):
                    self._goods_detail.append(i)
                else:
                    self._goods_detail.append(GoodsDetail.from_alipay_dict(i))
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def need_query_anti_rank(self):
        return self._need_query_anti_rank

    @need_query_anti_rank.setter
    def need_query_anti_rank(self, value):
        self._need_query_anti_rank = value
    @property
    def need_query_marketing_rank(self):
        return self._need_query_marketing_rank

    @need_query_marketing_rank.setter
    def need_query_marketing_rank(self, value):
        self._need_query_marketing_rank = value
    @property
    def need_return_tag(self):
        return self._need_return_tag

    @need_return_tag.setter
    def need_return_tag(self, value):
        self._need_return_tag = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        self._promo_params = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.blind_mobile:
            if hasattr(self.blind_mobile, 'to_alipay_dict'):
                params['blind_mobile'] = self.blind_mobile.to_alipay_dict()
            else:
                params['blind_mobile'] = self.blind_mobile
        if self.confused_mobile_list:
            if isinstance(self.confused_mobile_list, list):
                for i in range(0, len(self.confused_mobile_list)):
                    element = self.confused_mobile_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.confused_mobile_list[i] = element.to_alipay_dict()
            if hasattr(self.confused_mobile_list, 'to_alipay_dict'):
                params['confused_mobile_list'] = self.confused_mobile_list.to_alipay_dict()
            else:
                params['confused_mobile_list'] = self.confused_mobile_list
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.encrypted_mobile:
            if hasattr(self.encrypted_mobile, 'to_alipay_dict'):
                params['encrypted_mobile'] = self.encrypted_mobile.to_alipay_dict()
            else:
                params['encrypted_mobile'] = self.encrypted_mobile
        if self.goods_detail:
            if isinstance(self.goods_detail, list):
                for i in range(0, len(self.goods_detail)):
                    element = self.goods_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.need_query_anti_rank:
            if hasattr(self.need_query_anti_rank, 'to_alipay_dict'):
                params['need_query_anti_rank'] = self.need_query_anti_rank.to_alipay_dict()
            else:
                params['need_query_anti_rank'] = self.need_query_anti_rank
        if self.need_query_marketing_rank:
            if hasattr(self.need_query_marketing_rank, 'to_alipay_dict'):
                params['need_query_marketing_rank'] = self.need_query_marketing_rank.to_alipay_dict()
            else:
                params['need_query_marketing_rank'] = self.need_query_marketing_rank
        if self.need_return_tag:
            if hasattr(self.need_return_tag, 'to_alipay_dict'):
                params['need_return_tag'] = self.need_return_tag.to_alipay_dict()
            else:
                params['need_return_tag'] = self.need_return_tag
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppMarketingConsultModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'blind_mobile' in d:
            o.blind_mobile = d['blind_mobile']
        if 'confused_mobile_list' in d:
            o.confused_mobile_list = d['confused_mobile_list']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'encrypted_mobile' in d:
            o.encrypted_mobile = d['encrypted_mobile']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'need_query_anti_rank' in d:
            o.need_query_anti_rank = d['need_query_anti_rank']
        if 'need_query_marketing_rank' in d:
            o.need_query_marketing_rank = d['need_query_marketing_rank']
        if 'need_return_tag' in d:
            o.need_return_tag = d['need_return_tag']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'undiscountable_amount' in d:
            o.undiscountable_amount = d['undiscountable_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


