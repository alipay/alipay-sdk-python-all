#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountDstCampPrizeModel import DiscountDstCampPrizeModel
from alipay.aop.api.domain.DstCampRuleModel import DstCampRuleModel
from alipay.aop.api.domain.DateAreaModel import DateAreaModel
from alipay.aop.api.domain.RandomDiscountDstCampPrizeModel import RandomDiscountDstCampPrizeModel
from alipay.aop.api.domain.ReduceDstCampPrizeModel import ReduceDstCampPrizeModel
from alipay.aop.api.domain.ReduceToDiscountDstCampPrizeModel import ReduceToDiscountDstCampPrizeModel
from alipay.aop.api.domain.ResetZeroDstCampPrizeModel import ResetZeroDstCampPrizeModel
from alipay.aop.api.domain.SingleDstCampPrizeModel import SingleDstCampPrizeModel
from alipay.aop.api.domain.StagedDiscountDstCampPrizeModel import StagedDiscountDstCampPrizeModel


class AlipayMarketingCampaignDiscountOperateModel(object):

    def __init__(self):
        self._camp_code = None
        self._camp_desc = None
        self._camp_id = None
        self._camp_name = None
        self._camp_slogan = None
        self._discount_dst_camp_prize_model = None
        self._dst_camp_rule_model = None
        self._dst_camp_sub_time_model_list = None
        self._gmt_end = None
        self._gmt_start = None
        self._operate_type = None
        self._prize_type = None
        self._random_discount_dst_camp_prize_model = None
        self._reduce_dst_camp_prize_model = None
        self._reduce_to_discount_dst_camp_prize_model = None
        self._reset_zero_dst_camp_prize_model = None
        self._single_dst_camp_prize_model = None
        self._staged_discount_dst_camp_prize_model = None

    @property
    def camp_code(self):
        return self._camp_code

    @camp_code.setter
    def camp_code(self, value):
        self._camp_code = value
    @property
    def camp_desc(self):
        return self._camp_desc

    @camp_desc.setter
    def camp_desc(self, value):
        self._camp_desc = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_name(self):
        return self._camp_name

    @camp_name.setter
    def camp_name(self, value):
        self._camp_name = value
    @property
    def camp_slogan(self):
        return self._camp_slogan

    @camp_slogan.setter
    def camp_slogan(self, value):
        self._camp_slogan = value
    @property
    def discount_dst_camp_prize_model(self):
        return self._discount_dst_camp_prize_model

    @discount_dst_camp_prize_model.setter
    def discount_dst_camp_prize_model(self, value):
        if isinstance(value, DiscountDstCampPrizeModel):
            self._discount_dst_camp_prize_model = value
        else:
            self._discount_dst_camp_prize_model = DiscountDstCampPrizeModel.from_alipay_dict(value)
    @property
    def dst_camp_rule_model(self):
        return self._dst_camp_rule_model

    @dst_camp_rule_model.setter
    def dst_camp_rule_model(self, value):
        if isinstance(value, DstCampRuleModel):
            self._dst_camp_rule_model = value
        else:
            self._dst_camp_rule_model = DstCampRuleModel.from_alipay_dict(value)
    @property
    def dst_camp_sub_time_model_list(self):
        return self._dst_camp_sub_time_model_list

    @dst_camp_sub_time_model_list.setter
    def dst_camp_sub_time_model_list(self, value):
        if isinstance(value, list):
            self._dst_camp_sub_time_model_list = list()
            for i in value:
                if isinstance(i, DateAreaModel):
                    self._dst_camp_sub_time_model_list.append(i)
                else:
                    self._dst_camp_sub_time_model_list.append(DateAreaModel.from_alipay_dict(i))
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def random_discount_dst_camp_prize_model(self):
        return self._random_discount_dst_camp_prize_model

    @random_discount_dst_camp_prize_model.setter
    def random_discount_dst_camp_prize_model(self, value):
        if isinstance(value, RandomDiscountDstCampPrizeModel):
            self._random_discount_dst_camp_prize_model = value
        else:
            self._random_discount_dst_camp_prize_model = RandomDiscountDstCampPrizeModel.from_alipay_dict(value)
    @property
    def reduce_dst_camp_prize_model(self):
        return self._reduce_dst_camp_prize_model

    @reduce_dst_camp_prize_model.setter
    def reduce_dst_camp_prize_model(self, value):
        if isinstance(value, ReduceDstCampPrizeModel):
            self._reduce_dst_camp_prize_model = value
        else:
            self._reduce_dst_camp_prize_model = ReduceDstCampPrizeModel.from_alipay_dict(value)
    @property
    def reduce_to_discount_dst_camp_prize_model(self):
        return self._reduce_to_discount_dst_camp_prize_model

    @reduce_to_discount_dst_camp_prize_model.setter
    def reduce_to_discount_dst_camp_prize_model(self, value):
        if isinstance(value, ReduceToDiscountDstCampPrizeModel):
            self._reduce_to_discount_dst_camp_prize_model = value
        else:
            self._reduce_to_discount_dst_camp_prize_model = ReduceToDiscountDstCampPrizeModel.from_alipay_dict(value)
    @property
    def reset_zero_dst_camp_prize_model(self):
        return self._reset_zero_dst_camp_prize_model

    @reset_zero_dst_camp_prize_model.setter
    def reset_zero_dst_camp_prize_model(self, value):
        if isinstance(value, ResetZeroDstCampPrizeModel):
            self._reset_zero_dst_camp_prize_model = value
        else:
            self._reset_zero_dst_camp_prize_model = ResetZeroDstCampPrizeModel.from_alipay_dict(value)
    @property
    def single_dst_camp_prize_model(self):
        return self._single_dst_camp_prize_model

    @single_dst_camp_prize_model.setter
    def single_dst_camp_prize_model(self, value):
        if isinstance(value, SingleDstCampPrizeModel):
            self._single_dst_camp_prize_model = value
        else:
            self._single_dst_camp_prize_model = SingleDstCampPrizeModel.from_alipay_dict(value)
    @property
    def staged_discount_dst_camp_prize_model(self):
        return self._staged_discount_dst_camp_prize_model

    @staged_discount_dst_camp_prize_model.setter
    def staged_discount_dst_camp_prize_model(self, value):
        if isinstance(value, StagedDiscountDstCampPrizeModel):
            self._staged_discount_dst_camp_prize_model = value
        else:
            self._staged_discount_dst_camp_prize_model = StagedDiscountDstCampPrizeModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.camp_code:
            if hasattr(self.camp_code, 'to_alipay_dict'):
                params['camp_code'] = self.camp_code.to_alipay_dict()
            else:
                params['camp_code'] = self.camp_code
        if self.camp_desc:
            if hasattr(self.camp_desc, 'to_alipay_dict'):
                params['camp_desc'] = self.camp_desc.to_alipay_dict()
            else:
                params['camp_desc'] = self.camp_desc
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_name:
            if hasattr(self.camp_name, 'to_alipay_dict'):
                params['camp_name'] = self.camp_name.to_alipay_dict()
            else:
                params['camp_name'] = self.camp_name
        if self.camp_slogan:
            if hasattr(self.camp_slogan, 'to_alipay_dict'):
                params['camp_slogan'] = self.camp_slogan.to_alipay_dict()
            else:
                params['camp_slogan'] = self.camp_slogan
        if self.discount_dst_camp_prize_model:
            if hasattr(self.discount_dst_camp_prize_model, 'to_alipay_dict'):
                params['discount_dst_camp_prize_model'] = self.discount_dst_camp_prize_model.to_alipay_dict()
            else:
                params['discount_dst_camp_prize_model'] = self.discount_dst_camp_prize_model
        if self.dst_camp_rule_model:
            if hasattr(self.dst_camp_rule_model, 'to_alipay_dict'):
                params['dst_camp_rule_model'] = self.dst_camp_rule_model.to_alipay_dict()
            else:
                params['dst_camp_rule_model'] = self.dst_camp_rule_model
        if self.dst_camp_sub_time_model_list:
            if isinstance(self.dst_camp_sub_time_model_list, list):
                for i in range(0, len(self.dst_camp_sub_time_model_list)):
                    element = self.dst_camp_sub_time_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dst_camp_sub_time_model_list[i] = element.to_alipay_dict()
            if hasattr(self.dst_camp_sub_time_model_list, 'to_alipay_dict'):
                params['dst_camp_sub_time_model_list'] = self.dst_camp_sub_time_model_list.to_alipay_dict()
            else:
                params['dst_camp_sub_time_model_list'] = self.dst_camp_sub_time_model_list
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.random_discount_dst_camp_prize_model:
            if hasattr(self.random_discount_dst_camp_prize_model, 'to_alipay_dict'):
                params['random_discount_dst_camp_prize_model'] = self.random_discount_dst_camp_prize_model.to_alipay_dict()
            else:
                params['random_discount_dst_camp_prize_model'] = self.random_discount_dst_camp_prize_model
        if self.reduce_dst_camp_prize_model:
            if hasattr(self.reduce_dst_camp_prize_model, 'to_alipay_dict'):
                params['reduce_dst_camp_prize_model'] = self.reduce_dst_camp_prize_model.to_alipay_dict()
            else:
                params['reduce_dst_camp_prize_model'] = self.reduce_dst_camp_prize_model
        if self.reduce_to_discount_dst_camp_prize_model:
            if hasattr(self.reduce_to_discount_dst_camp_prize_model, 'to_alipay_dict'):
                params['reduce_to_discount_dst_camp_prize_model'] = self.reduce_to_discount_dst_camp_prize_model.to_alipay_dict()
            else:
                params['reduce_to_discount_dst_camp_prize_model'] = self.reduce_to_discount_dst_camp_prize_model
        if self.reset_zero_dst_camp_prize_model:
            if hasattr(self.reset_zero_dst_camp_prize_model, 'to_alipay_dict'):
                params['reset_zero_dst_camp_prize_model'] = self.reset_zero_dst_camp_prize_model.to_alipay_dict()
            else:
                params['reset_zero_dst_camp_prize_model'] = self.reset_zero_dst_camp_prize_model
        if self.single_dst_camp_prize_model:
            if hasattr(self.single_dst_camp_prize_model, 'to_alipay_dict'):
                params['single_dst_camp_prize_model'] = self.single_dst_camp_prize_model.to_alipay_dict()
            else:
                params['single_dst_camp_prize_model'] = self.single_dst_camp_prize_model
        if self.staged_discount_dst_camp_prize_model:
            if hasattr(self.staged_discount_dst_camp_prize_model, 'to_alipay_dict'):
                params['staged_discount_dst_camp_prize_model'] = self.staged_discount_dst_camp_prize_model.to_alipay_dict()
            else:
                params['staged_discount_dst_camp_prize_model'] = self.staged_discount_dst_camp_prize_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDiscountOperateModel()
        if 'camp_code' in d:
            o.camp_code = d['camp_code']
        if 'camp_desc' in d:
            o.camp_desc = d['camp_desc']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_name' in d:
            o.camp_name = d['camp_name']
        if 'camp_slogan' in d:
            o.camp_slogan = d['camp_slogan']
        if 'discount_dst_camp_prize_model' in d:
            o.discount_dst_camp_prize_model = d['discount_dst_camp_prize_model']
        if 'dst_camp_rule_model' in d:
            o.dst_camp_rule_model = d['dst_camp_rule_model']
        if 'dst_camp_sub_time_model_list' in d:
            o.dst_camp_sub_time_model_list = d['dst_camp_sub_time_model_list']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'random_discount_dst_camp_prize_model' in d:
            o.random_discount_dst_camp_prize_model = d['random_discount_dst_camp_prize_model']
        if 'reduce_dst_camp_prize_model' in d:
            o.reduce_dst_camp_prize_model = d['reduce_dst_camp_prize_model']
        if 'reduce_to_discount_dst_camp_prize_model' in d:
            o.reduce_to_discount_dst_camp_prize_model = d['reduce_to_discount_dst_camp_prize_model']
        if 'reset_zero_dst_camp_prize_model' in d:
            o.reset_zero_dst_camp_prize_model = d['reset_zero_dst_camp_prize_model']
        if 'single_dst_camp_prize_model' in d:
            o.single_dst_camp_prize_model = d['single_dst_camp_prize_model']
        if 'staged_discount_dst_camp_prize_model' in d:
            o.staged_discount_dst_camp_prize_model = d['staged_discount_dst_camp_prize_model']
        return o


