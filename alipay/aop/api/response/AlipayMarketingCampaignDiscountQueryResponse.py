#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountDstCampPrizeModel import DiscountDstCampPrizeModel
from alipay.aop.api.domain.DstCampRuleModel import DstCampRuleModel
from alipay.aop.api.domain.DateAreaModel import DateAreaModel
from alipay.aop.api.domain.RandomDiscountDstCampPrizeModel import RandomDiscountDstCampPrizeModel
from alipay.aop.api.domain.ReduceDstCampPrizeModel import ReduceDstCampPrizeModel
from alipay.aop.api.domain.ReduceToDiscountDstCampPrizeModel import ReduceToDiscountDstCampPrizeModel
from alipay.aop.api.domain.ResetZeroDstCampPrizeModel import ResetZeroDstCampPrizeModel
from alipay.aop.api.domain.SingleDstCampPrizeModel import SingleDstCampPrizeModel
from alipay.aop.api.domain.StagedDiscountDstCampPrizeModel import StagedDiscountDstCampPrizeModel


class AlipayMarketingCampaignDiscountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDiscountQueryResponse, self).__init__()
        self._camp_code = None
        self._camp_desc = None
        self._camp_id = None
        self._camp_name = None
        self._camp_slogan = None
        self._camp_status = None
        self._discount_dst_camp_prize_model = None
        self._dst_camp_rule_model = None
        self._dst_camp_sub_time_model_list = None
        self._gmt_end = None
        self._gmt_start = None
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
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDiscountQueryResponse, self).parse_response_content(response_content)
        if 'camp_code' in response:
            self.camp_code = response['camp_code']
        if 'camp_desc' in response:
            self.camp_desc = response['camp_desc']
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'camp_name' in response:
            self.camp_name = response['camp_name']
        if 'camp_slogan' in response:
            self.camp_slogan = response['camp_slogan']
        if 'camp_status' in response:
            self.camp_status = response['camp_status']
        if 'discount_dst_camp_prize_model' in response:
            self.discount_dst_camp_prize_model = response['discount_dst_camp_prize_model']
        if 'dst_camp_rule_model' in response:
            self.dst_camp_rule_model = response['dst_camp_rule_model']
        if 'dst_camp_sub_time_model_list' in response:
            self.dst_camp_sub_time_model_list = response['dst_camp_sub_time_model_list']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'prize_type' in response:
            self.prize_type = response['prize_type']
        if 'random_discount_dst_camp_prize_model' in response:
            self.random_discount_dst_camp_prize_model = response['random_discount_dst_camp_prize_model']
        if 'reduce_dst_camp_prize_model' in response:
            self.reduce_dst_camp_prize_model = response['reduce_dst_camp_prize_model']
        if 'reduce_to_discount_dst_camp_prize_model' in response:
            self.reduce_to_discount_dst_camp_prize_model = response['reduce_to_discount_dst_camp_prize_model']
        if 'reset_zero_dst_camp_prize_model' in response:
            self.reset_zero_dst_camp_prize_model = response['reset_zero_dst_camp_prize_model']
        if 'single_dst_camp_prize_model' in response:
            self.single_dst_camp_prize_model = response['single_dst_camp_prize_model']
        if 'staged_discount_dst_camp_prize_model' in response:
            self.staged_discount_dst_camp_prize_model = response['staged_discount_dst_camp_prize_model']
