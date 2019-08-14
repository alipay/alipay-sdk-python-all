#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KcpLeadsInfo(object):

    def __init__(self):
        self._buy_tips = None
        self._comment_count = None
        self._compare_label = None
        self._deal_id = None
        self._dish_list = None
        self._effective_date = None
        self._industry_type = None
        self._jd_shop_id = None
        self._kb_shop_ids = None
        self._leads_id = None
        self._minus_description = None
        self._price_rule = None
        self._rating = None
        self._sales = None
        self._tags = None
        self._title = None
        self._type = None
        self._unvalidate_info = None
        self._valitime_info = None
        self._ver = None

    @property
    def buy_tips(self):
        return self._buy_tips

    @buy_tips.setter
    def buy_tips(self, value):
        self._buy_tips = value
    @property
    def comment_count(self):
        return self._comment_count

    @comment_count.setter
    def comment_count(self, value):
        self._comment_count = value
    @property
    def compare_label(self):
        return self._compare_label

    @compare_label.setter
    def compare_label(self, value):
        self._compare_label = value
    @property
    def deal_id(self):
        return self._deal_id

    @deal_id.setter
    def deal_id(self, value):
        self._deal_id = value
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        self._dish_list = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def industry_type(self):
        return self._industry_type

    @industry_type.setter
    def industry_type(self, value):
        self._industry_type = value
    @property
    def jd_shop_id(self):
        return self._jd_shop_id

    @jd_shop_id.setter
    def jd_shop_id(self, value):
        self._jd_shop_id = value
    @property
    def kb_shop_ids(self):
        return self._kb_shop_ids

    @kb_shop_ids.setter
    def kb_shop_ids(self, value):
        if isinstance(value, list):
            self._kb_shop_ids = list()
            for i in value:
                self._kb_shop_ids.append(i)
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def minus_description(self):
        return self._minus_description

    @minus_description.setter
    def minus_description(self, value):
        self._minus_description = value
    @property
    def price_rule(self):
        return self._price_rule

    @price_rule.setter
    def price_rule(self, value):
        self._price_rule = value
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unvalidate_info(self):
        return self._unvalidate_info

    @unvalidate_info.setter
    def unvalidate_info(self, value):
        self._unvalidate_info = value
    @property
    def valitime_info(self):
        return self._valitime_info

    @valitime_info.setter
    def valitime_info(self, value):
        self._valitime_info = value
    @property
    def ver(self):
        return self._ver

    @ver.setter
    def ver(self, value):
        self._ver = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_tips:
            if hasattr(self.buy_tips, 'to_alipay_dict'):
                params['buy_tips'] = self.buy_tips.to_alipay_dict()
            else:
                params['buy_tips'] = self.buy_tips
        if self.comment_count:
            if hasattr(self.comment_count, 'to_alipay_dict'):
                params['comment_count'] = self.comment_count.to_alipay_dict()
            else:
                params['comment_count'] = self.comment_count
        if self.compare_label:
            if hasattr(self.compare_label, 'to_alipay_dict'):
                params['compare_label'] = self.compare_label.to_alipay_dict()
            else:
                params['compare_label'] = self.compare_label
        if self.deal_id:
            if hasattr(self.deal_id, 'to_alipay_dict'):
                params['deal_id'] = self.deal_id.to_alipay_dict()
            else:
                params['deal_id'] = self.deal_id
        if self.dish_list:
            if hasattr(self.dish_list, 'to_alipay_dict'):
                params['dish_list'] = self.dish_list.to_alipay_dict()
            else:
                params['dish_list'] = self.dish_list
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.industry_type:
            if hasattr(self.industry_type, 'to_alipay_dict'):
                params['industry_type'] = self.industry_type.to_alipay_dict()
            else:
                params['industry_type'] = self.industry_type
        if self.jd_shop_id:
            if hasattr(self.jd_shop_id, 'to_alipay_dict'):
                params['jd_shop_id'] = self.jd_shop_id.to_alipay_dict()
            else:
                params['jd_shop_id'] = self.jd_shop_id
        if self.kb_shop_ids:
            if isinstance(self.kb_shop_ids, list):
                for i in range(0, len(self.kb_shop_ids)):
                    element = self.kb_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kb_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.kb_shop_ids, 'to_alipay_dict'):
                params['kb_shop_ids'] = self.kb_shop_ids.to_alipay_dict()
            else:
                params['kb_shop_ids'] = self.kb_shop_ids
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.minus_description:
            if hasattr(self.minus_description, 'to_alipay_dict'):
                params['minus_description'] = self.minus_description.to_alipay_dict()
            else:
                params['minus_description'] = self.minus_description
        if self.price_rule:
            if hasattr(self.price_rule, 'to_alipay_dict'):
                params['price_rule'] = self.price_rule.to_alipay_dict()
            else:
                params['price_rule'] = self.price_rule
        if self.rating:
            if hasattr(self.rating, 'to_alipay_dict'):
                params['rating'] = self.rating.to_alipay_dict()
            else:
                params['rating'] = self.rating
        if self.sales:
            if hasattr(self.sales, 'to_alipay_dict'):
                params['sales'] = self.sales.to_alipay_dict()
            else:
                params['sales'] = self.sales
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.unvalidate_info:
            if hasattr(self.unvalidate_info, 'to_alipay_dict'):
                params['unvalidate_info'] = self.unvalidate_info.to_alipay_dict()
            else:
                params['unvalidate_info'] = self.unvalidate_info
        if self.valitime_info:
            if hasattr(self.valitime_info, 'to_alipay_dict'):
                params['valitime_info'] = self.valitime_info.to_alipay_dict()
            else:
                params['valitime_info'] = self.valitime_info
        if self.ver:
            if hasattr(self.ver, 'to_alipay_dict'):
                params['ver'] = self.ver.to_alipay_dict()
            else:
                params['ver'] = self.ver
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KcpLeadsInfo()
        if 'buy_tips' in d:
            o.buy_tips = d['buy_tips']
        if 'comment_count' in d:
            o.comment_count = d['comment_count']
        if 'compare_label' in d:
            o.compare_label = d['compare_label']
        if 'deal_id' in d:
            o.deal_id = d['deal_id']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'industry_type' in d:
            o.industry_type = d['industry_type']
        if 'jd_shop_id' in d:
            o.jd_shop_id = d['jd_shop_id']
        if 'kb_shop_ids' in d:
            o.kb_shop_ids = d['kb_shop_ids']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'minus_description' in d:
            o.minus_description = d['minus_description']
        if 'price_rule' in d:
            o.price_rule = d['price_rule']
        if 'rating' in d:
            o.rating = d['rating']
        if 'sales' in d:
            o.sales = d['sales']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        if 'unvalidate_info' in d:
            o.unvalidate_info = d['unvalidate_info']
        if 'valitime_info' in d:
            o.valitime_info = d['valitime_info']
        if 'ver' in d:
            o.ver = d['ver']
        return o


