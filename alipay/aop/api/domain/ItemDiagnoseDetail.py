#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemDiagnoseDetail(object):

    def __init__(self):
        self._hot_grade = None
        self._hot_value = None
        self._item_diagnose = None
        self._item_diagnose_desc = None
        self._item_id = None
        self._item_name = None
        self._item_price = None
        self._rec_ninety_consume_uid_cnt = None
        self._rec_ninety_rebuy_uid_cnt = None
        self._rec_seven_sale_amt = None
        self._rec_seven_sale_cnt = None
        self._rec_sixty_consume_uid_cnt = None
        self._rec_sixty_rebuy_uid_cnt = None
        self._rec_thirty_consume_uid_cnt = None
        self._rec_thirty_rebuy_uid_cnt = None
        self._rec_thirty_sale_amt = None
        self._rec_thirty_sale_cnt = None
        self._report_date = None

    @property
    def hot_grade(self):
        return self._hot_grade

    @hot_grade.setter
    def hot_grade(self, value):
        self._hot_grade = value
    @property
    def hot_value(self):
        return self._hot_value

    @hot_value.setter
    def hot_value(self, value):
        self._hot_value = value
    @property
    def item_diagnose(self):
        return self._item_diagnose

    @item_diagnose.setter
    def item_diagnose(self, value):
        self._item_diagnose = value
    @property
    def item_diagnose_desc(self):
        return self._item_diagnose_desc

    @item_diagnose_desc.setter
    def item_diagnose_desc(self, value):
        self._item_diagnose_desc = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def rec_ninety_consume_uid_cnt(self):
        return self._rec_ninety_consume_uid_cnt

    @rec_ninety_consume_uid_cnt.setter
    def rec_ninety_consume_uid_cnt(self, value):
        self._rec_ninety_consume_uid_cnt = value
    @property
    def rec_ninety_rebuy_uid_cnt(self):
        return self._rec_ninety_rebuy_uid_cnt

    @rec_ninety_rebuy_uid_cnt.setter
    def rec_ninety_rebuy_uid_cnt(self, value):
        self._rec_ninety_rebuy_uid_cnt = value
    @property
    def rec_seven_sale_amt(self):
        return self._rec_seven_sale_amt

    @rec_seven_sale_amt.setter
    def rec_seven_sale_amt(self, value):
        self._rec_seven_sale_amt = value
    @property
    def rec_seven_sale_cnt(self):
        return self._rec_seven_sale_cnt

    @rec_seven_sale_cnt.setter
    def rec_seven_sale_cnt(self, value):
        self._rec_seven_sale_cnt = value
    @property
    def rec_sixty_consume_uid_cnt(self):
        return self._rec_sixty_consume_uid_cnt

    @rec_sixty_consume_uid_cnt.setter
    def rec_sixty_consume_uid_cnt(self, value):
        self._rec_sixty_consume_uid_cnt = value
    @property
    def rec_sixty_rebuy_uid_cnt(self):
        return self._rec_sixty_rebuy_uid_cnt

    @rec_sixty_rebuy_uid_cnt.setter
    def rec_sixty_rebuy_uid_cnt(self, value):
        self._rec_sixty_rebuy_uid_cnt = value
    @property
    def rec_thirty_consume_uid_cnt(self):
        return self._rec_thirty_consume_uid_cnt

    @rec_thirty_consume_uid_cnt.setter
    def rec_thirty_consume_uid_cnt(self, value):
        self._rec_thirty_consume_uid_cnt = value
    @property
    def rec_thirty_rebuy_uid_cnt(self):
        return self._rec_thirty_rebuy_uid_cnt

    @rec_thirty_rebuy_uid_cnt.setter
    def rec_thirty_rebuy_uid_cnt(self, value):
        self._rec_thirty_rebuy_uid_cnt = value
    @property
    def rec_thirty_sale_amt(self):
        return self._rec_thirty_sale_amt

    @rec_thirty_sale_amt.setter
    def rec_thirty_sale_amt(self, value):
        self._rec_thirty_sale_amt = value
    @property
    def rec_thirty_sale_cnt(self):
        return self._rec_thirty_sale_cnt

    @rec_thirty_sale_cnt.setter
    def rec_thirty_sale_cnt(self, value):
        self._rec_thirty_sale_cnt = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.hot_grade:
            if hasattr(self.hot_grade, 'to_alipay_dict'):
                params['hot_grade'] = self.hot_grade.to_alipay_dict()
            else:
                params['hot_grade'] = self.hot_grade
        if self.hot_value:
            if hasattr(self.hot_value, 'to_alipay_dict'):
                params['hot_value'] = self.hot_value.to_alipay_dict()
            else:
                params['hot_value'] = self.hot_value
        if self.item_diagnose:
            if hasattr(self.item_diagnose, 'to_alipay_dict'):
                params['item_diagnose'] = self.item_diagnose.to_alipay_dict()
            else:
                params['item_diagnose'] = self.item_diagnose
        if self.item_diagnose_desc:
            if hasattr(self.item_diagnose_desc, 'to_alipay_dict'):
                params['item_diagnose_desc'] = self.item_diagnose_desc.to_alipay_dict()
            else:
                params['item_diagnose_desc'] = self.item_diagnose_desc
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.rec_ninety_consume_uid_cnt:
            if hasattr(self.rec_ninety_consume_uid_cnt, 'to_alipay_dict'):
                params['rec_ninety_consume_uid_cnt'] = self.rec_ninety_consume_uid_cnt.to_alipay_dict()
            else:
                params['rec_ninety_consume_uid_cnt'] = self.rec_ninety_consume_uid_cnt
        if self.rec_ninety_rebuy_uid_cnt:
            if hasattr(self.rec_ninety_rebuy_uid_cnt, 'to_alipay_dict'):
                params['rec_ninety_rebuy_uid_cnt'] = self.rec_ninety_rebuy_uid_cnt.to_alipay_dict()
            else:
                params['rec_ninety_rebuy_uid_cnt'] = self.rec_ninety_rebuy_uid_cnt
        if self.rec_seven_sale_amt:
            if hasattr(self.rec_seven_sale_amt, 'to_alipay_dict'):
                params['rec_seven_sale_amt'] = self.rec_seven_sale_amt.to_alipay_dict()
            else:
                params['rec_seven_sale_amt'] = self.rec_seven_sale_amt
        if self.rec_seven_sale_cnt:
            if hasattr(self.rec_seven_sale_cnt, 'to_alipay_dict'):
                params['rec_seven_sale_cnt'] = self.rec_seven_sale_cnt.to_alipay_dict()
            else:
                params['rec_seven_sale_cnt'] = self.rec_seven_sale_cnt
        if self.rec_sixty_consume_uid_cnt:
            if hasattr(self.rec_sixty_consume_uid_cnt, 'to_alipay_dict'):
                params['rec_sixty_consume_uid_cnt'] = self.rec_sixty_consume_uid_cnt.to_alipay_dict()
            else:
                params['rec_sixty_consume_uid_cnt'] = self.rec_sixty_consume_uid_cnt
        if self.rec_sixty_rebuy_uid_cnt:
            if hasattr(self.rec_sixty_rebuy_uid_cnt, 'to_alipay_dict'):
                params['rec_sixty_rebuy_uid_cnt'] = self.rec_sixty_rebuy_uid_cnt.to_alipay_dict()
            else:
                params['rec_sixty_rebuy_uid_cnt'] = self.rec_sixty_rebuy_uid_cnt
        if self.rec_thirty_consume_uid_cnt:
            if hasattr(self.rec_thirty_consume_uid_cnt, 'to_alipay_dict'):
                params['rec_thirty_consume_uid_cnt'] = self.rec_thirty_consume_uid_cnt.to_alipay_dict()
            else:
                params['rec_thirty_consume_uid_cnt'] = self.rec_thirty_consume_uid_cnt
        if self.rec_thirty_rebuy_uid_cnt:
            if hasattr(self.rec_thirty_rebuy_uid_cnt, 'to_alipay_dict'):
                params['rec_thirty_rebuy_uid_cnt'] = self.rec_thirty_rebuy_uid_cnt.to_alipay_dict()
            else:
                params['rec_thirty_rebuy_uid_cnt'] = self.rec_thirty_rebuy_uid_cnt
        if self.rec_thirty_sale_amt:
            if hasattr(self.rec_thirty_sale_amt, 'to_alipay_dict'):
                params['rec_thirty_sale_amt'] = self.rec_thirty_sale_amt.to_alipay_dict()
            else:
                params['rec_thirty_sale_amt'] = self.rec_thirty_sale_amt
        if self.rec_thirty_sale_cnt:
            if hasattr(self.rec_thirty_sale_cnt, 'to_alipay_dict'):
                params['rec_thirty_sale_cnt'] = self.rec_thirty_sale_cnt.to_alipay_dict()
            else:
                params['rec_thirty_sale_cnt'] = self.rec_thirty_sale_cnt
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDiagnoseDetail()
        if 'hot_grade' in d:
            o.hot_grade = d['hot_grade']
        if 'hot_value' in d:
            o.hot_value = d['hot_value']
        if 'item_diagnose' in d:
            o.item_diagnose = d['item_diagnose']
        if 'item_diagnose_desc' in d:
            o.item_diagnose_desc = d['item_diagnose_desc']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'rec_ninety_consume_uid_cnt' in d:
            o.rec_ninety_consume_uid_cnt = d['rec_ninety_consume_uid_cnt']
        if 'rec_ninety_rebuy_uid_cnt' in d:
            o.rec_ninety_rebuy_uid_cnt = d['rec_ninety_rebuy_uid_cnt']
        if 'rec_seven_sale_amt' in d:
            o.rec_seven_sale_amt = d['rec_seven_sale_amt']
        if 'rec_seven_sale_cnt' in d:
            o.rec_seven_sale_cnt = d['rec_seven_sale_cnt']
        if 'rec_sixty_consume_uid_cnt' in d:
            o.rec_sixty_consume_uid_cnt = d['rec_sixty_consume_uid_cnt']
        if 'rec_sixty_rebuy_uid_cnt' in d:
            o.rec_sixty_rebuy_uid_cnt = d['rec_sixty_rebuy_uid_cnt']
        if 'rec_thirty_consume_uid_cnt' in d:
            o.rec_thirty_consume_uid_cnt = d['rec_thirty_consume_uid_cnt']
        if 'rec_thirty_rebuy_uid_cnt' in d:
            o.rec_thirty_rebuy_uid_cnt = d['rec_thirty_rebuy_uid_cnt']
        if 'rec_thirty_sale_amt' in d:
            o.rec_thirty_sale_amt = d['rec_thirty_sale_amt']
        if 'rec_thirty_sale_cnt' in d:
            o.rec_thirty_sale_cnt = d['rec_thirty_sale_cnt']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


