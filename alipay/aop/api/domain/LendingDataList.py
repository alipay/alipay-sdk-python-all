#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LendingDataList(object):

    def __init__(self):
        self._curr_fba_inv_value = None
        self._currency = None
        self._disbursements_eight_m = None
        self._disbursements_eight_q = None
        self._disbursements_eleven_m = None
        self._disbursements_five_m = None
        self._disbursements_five_q = None
        self._disbursements_five_w = None
        self._disbursements_four_m = None
        self._disbursements_four_q = None
        self._disbursements_four_w = None
        self._disbursements_nine_m = None
        self._disbursements_one_m = None
        self._disbursements_one_q = None
        self._disbursements_one_w = None
        self._disbursements_one_y = None
        self._disbursements_seven_m = None
        self._disbursements_seven_q = None
        self._disbursements_six_m = None
        self._disbursements_six_q = None
        self._disbursements_six_w = None
        self._disbursements_ten_m = None
        self._disbursements_three_m = None
        self._disbursements_three_q = None
        self._disbursements_three_w = None
        self._disbursements_twelve_m = None
        self._disbursements_two_m = None
        self._disbursements_two_q = None
        self._disbursements_two_w = None
        self._disbursements_two_y = None
        self._marketplace_country = None
        self._offer_id = None
        self._primary_category_last_three_month_sales_value = None
        self._primary_product_category = None
        self._report_card_data_date = None
        self._sales_eight_m = None
        self._sales_eight_q = None
        self._sales_eleven_m = None
        self._sales_five_m = None
        self._sales_five_q = None
        self._sales_five_w = None
        self._sales_four_m = None
        self._sales_four_q = None
        self._sales_four_w = None
        self._sales_nine_m = None
        self._sales_one_m = None
        self._sales_one_q = None
        self._sales_one_w = None
        self._sales_one_y = None
        self._sales_seven_m = None
        self._sales_seven_q = None
        self._sales_six_m = None
        self._sales_six_q = None
        self._sales_six_w = None
        self._sales_stability_score = None
        self._sales_ten_m = None
        self._sales_three_m = None
        self._sales_three_q = None
        self._sales_three_w = None
        self._sales_twelve_m = None
        self._sales_two_m = None
        self._sales_two_q = None
        self._sales_two_w = None
        self._sales_two_y = None
        self._seller_status = None
        self._t_thirteen_wk_fba = None
        self._t_three_m_fba_inv_value = None
        self._tenure = None
        self._ttm_cancellations = None
        self._ttm_enforcements = None
        self._ttm_feedback = None
        self._ttm_late_shipments = None
        self._ttm_neg_feedback = None
        self._ttm_order_defects = None
        self._ttm_orders = None
        self._ttm_returns = None

    @property
    def curr_fba_inv_value(self):
        return self._curr_fba_inv_value

    @curr_fba_inv_value.setter
    def curr_fba_inv_value(self, value):
        self._curr_fba_inv_value = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def disbursements_eight_m(self):
        return self._disbursements_eight_m

    @disbursements_eight_m.setter
    def disbursements_eight_m(self, value):
        self._disbursements_eight_m = value
    @property
    def disbursements_eight_q(self):
        return self._disbursements_eight_q

    @disbursements_eight_q.setter
    def disbursements_eight_q(self, value):
        self._disbursements_eight_q = value
    @property
    def disbursements_eleven_m(self):
        return self._disbursements_eleven_m

    @disbursements_eleven_m.setter
    def disbursements_eleven_m(self, value):
        self._disbursements_eleven_m = value
    @property
    def disbursements_five_m(self):
        return self._disbursements_five_m

    @disbursements_five_m.setter
    def disbursements_five_m(self, value):
        self._disbursements_five_m = value
    @property
    def disbursements_five_q(self):
        return self._disbursements_five_q

    @disbursements_five_q.setter
    def disbursements_five_q(self, value):
        self._disbursements_five_q = value
    @property
    def disbursements_five_w(self):
        return self._disbursements_five_w

    @disbursements_five_w.setter
    def disbursements_five_w(self, value):
        self._disbursements_five_w = value
    @property
    def disbursements_four_m(self):
        return self._disbursements_four_m

    @disbursements_four_m.setter
    def disbursements_four_m(self, value):
        self._disbursements_four_m = value
    @property
    def disbursements_four_q(self):
        return self._disbursements_four_q

    @disbursements_four_q.setter
    def disbursements_four_q(self, value):
        self._disbursements_four_q = value
    @property
    def disbursements_four_w(self):
        return self._disbursements_four_w

    @disbursements_four_w.setter
    def disbursements_four_w(self, value):
        self._disbursements_four_w = value
    @property
    def disbursements_nine_m(self):
        return self._disbursements_nine_m

    @disbursements_nine_m.setter
    def disbursements_nine_m(self, value):
        self._disbursements_nine_m = value
    @property
    def disbursements_one_m(self):
        return self._disbursements_one_m

    @disbursements_one_m.setter
    def disbursements_one_m(self, value):
        self._disbursements_one_m = value
    @property
    def disbursements_one_q(self):
        return self._disbursements_one_q

    @disbursements_one_q.setter
    def disbursements_one_q(self, value):
        self._disbursements_one_q = value
    @property
    def disbursements_one_w(self):
        return self._disbursements_one_w

    @disbursements_one_w.setter
    def disbursements_one_w(self, value):
        self._disbursements_one_w = value
    @property
    def disbursements_one_y(self):
        return self._disbursements_one_y

    @disbursements_one_y.setter
    def disbursements_one_y(self, value):
        self._disbursements_one_y = value
    @property
    def disbursements_seven_m(self):
        return self._disbursements_seven_m

    @disbursements_seven_m.setter
    def disbursements_seven_m(self, value):
        self._disbursements_seven_m = value
    @property
    def disbursements_seven_q(self):
        return self._disbursements_seven_q

    @disbursements_seven_q.setter
    def disbursements_seven_q(self, value):
        self._disbursements_seven_q = value
    @property
    def disbursements_six_m(self):
        return self._disbursements_six_m

    @disbursements_six_m.setter
    def disbursements_six_m(self, value):
        self._disbursements_six_m = value
    @property
    def disbursements_six_q(self):
        return self._disbursements_six_q

    @disbursements_six_q.setter
    def disbursements_six_q(self, value):
        self._disbursements_six_q = value
    @property
    def disbursements_six_w(self):
        return self._disbursements_six_w

    @disbursements_six_w.setter
    def disbursements_six_w(self, value):
        self._disbursements_six_w = value
    @property
    def disbursements_ten_m(self):
        return self._disbursements_ten_m

    @disbursements_ten_m.setter
    def disbursements_ten_m(self, value):
        self._disbursements_ten_m = value
    @property
    def disbursements_three_m(self):
        return self._disbursements_three_m

    @disbursements_three_m.setter
    def disbursements_three_m(self, value):
        self._disbursements_three_m = value
    @property
    def disbursements_three_q(self):
        return self._disbursements_three_q

    @disbursements_three_q.setter
    def disbursements_three_q(self, value):
        self._disbursements_three_q = value
    @property
    def disbursements_three_w(self):
        return self._disbursements_three_w

    @disbursements_three_w.setter
    def disbursements_three_w(self, value):
        self._disbursements_three_w = value
    @property
    def disbursements_twelve_m(self):
        return self._disbursements_twelve_m

    @disbursements_twelve_m.setter
    def disbursements_twelve_m(self, value):
        self._disbursements_twelve_m = value
    @property
    def disbursements_two_m(self):
        return self._disbursements_two_m

    @disbursements_two_m.setter
    def disbursements_two_m(self, value):
        self._disbursements_two_m = value
    @property
    def disbursements_two_q(self):
        return self._disbursements_two_q

    @disbursements_two_q.setter
    def disbursements_two_q(self, value):
        self._disbursements_two_q = value
    @property
    def disbursements_two_w(self):
        return self._disbursements_two_w

    @disbursements_two_w.setter
    def disbursements_two_w(self, value):
        self._disbursements_two_w = value
    @property
    def disbursements_two_y(self):
        return self._disbursements_two_y

    @disbursements_two_y.setter
    def disbursements_two_y(self, value):
        self._disbursements_two_y = value
    @property
    def marketplace_country(self):
        return self._marketplace_country

    @marketplace_country.setter
    def marketplace_country(self, value):
        self._marketplace_country = value
    @property
    def offer_id(self):
        return self._offer_id

    @offer_id.setter
    def offer_id(self, value):
        self._offer_id = value
    @property
    def primary_category_last_three_month_sales_value(self):
        return self._primary_category_last_three_month_sales_value

    @primary_category_last_three_month_sales_value.setter
    def primary_category_last_three_month_sales_value(self, value):
        self._primary_category_last_three_month_sales_value = value
    @property
    def primary_product_category(self):
        return self._primary_product_category

    @primary_product_category.setter
    def primary_product_category(self, value):
        self._primary_product_category = value
    @property
    def report_card_data_date(self):
        return self._report_card_data_date

    @report_card_data_date.setter
    def report_card_data_date(self, value):
        self._report_card_data_date = value
    @property
    def sales_eight_m(self):
        return self._sales_eight_m

    @sales_eight_m.setter
    def sales_eight_m(self, value):
        self._sales_eight_m = value
    @property
    def sales_eight_q(self):
        return self._sales_eight_q

    @sales_eight_q.setter
    def sales_eight_q(self, value):
        self._sales_eight_q = value
    @property
    def sales_eleven_m(self):
        return self._sales_eleven_m

    @sales_eleven_m.setter
    def sales_eleven_m(self, value):
        self._sales_eleven_m = value
    @property
    def sales_five_m(self):
        return self._sales_five_m

    @sales_five_m.setter
    def sales_five_m(self, value):
        self._sales_five_m = value
    @property
    def sales_five_q(self):
        return self._sales_five_q

    @sales_five_q.setter
    def sales_five_q(self, value):
        self._sales_five_q = value
    @property
    def sales_five_w(self):
        return self._sales_five_w

    @sales_five_w.setter
    def sales_five_w(self, value):
        self._sales_five_w = value
    @property
    def sales_four_m(self):
        return self._sales_four_m

    @sales_four_m.setter
    def sales_four_m(self, value):
        self._sales_four_m = value
    @property
    def sales_four_q(self):
        return self._sales_four_q

    @sales_four_q.setter
    def sales_four_q(self, value):
        self._sales_four_q = value
    @property
    def sales_four_w(self):
        return self._sales_four_w

    @sales_four_w.setter
    def sales_four_w(self, value):
        self._sales_four_w = value
    @property
    def sales_nine_m(self):
        return self._sales_nine_m

    @sales_nine_m.setter
    def sales_nine_m(self, value):
        self._sales_nine_m = value
    @property
    def sales_one_m(self):
        return self._sales_one_m

    @sales_one_m.setter
    def sales_one_m(self, value):
        self._sales_one_m = value
    @property
    def sales_one_q(self):
        return self._sales_one_q

    @sales_one_q.setter
    def sales_one_q(self, value):
        self._sales_one_q = value
    @property
    def sales_one_w(self):
        return self._sales_one_w

    @sales_one_w.setter
    def sales_one_w(self, value):
        self._sales_one_w = value
    @property
    def sales_one_y(self):
        return self._sales_one_y

    @sales_one_y.setter
    def sales_one_y(self, value):
        self._sales_one_y = value
    @property
    def sales_seven_m(self):
        return self._sales_seven_m

    @sales_seven_m.setter
    def sales_seven_m(self, value):
        self._sales_seven_m = value
    @property
    def sales_seven_q(self):
        return self._sales_seven_q

    @sales_seven_q.setter
    def sales_seven_q(self, value):
        self._sales_seven_q = value
    @property
    def sales_six_m(self):
        return self._sales_six_m

    @sales_six_m.setter
    def sales_six_m(self, value):
        self._sales_six_m = value
    @property
    def sales_six_q(self):
        return self._sales_six_q

    @sales_six_q.setter
    def sales_six_q(self, value):
        self._sales_six_q = value
    @property
    def sales_six_w(self):
        return self._sales_six_w

    @sales_six_w.setter
    def sales_six_w(self, value):
        self._sales_six_w = value
    @property
    def sales_stability_score(self):
        return self._sales_stability_score

    @sales_stability_score.setter
    def sales_stability_score(self, value):
        self._sales_stability_score = value
    @property
    def sales_ten_m(self):
        return self._sales_ten_m

    @sales_ten_m.setter
    def sales_ten_m(self, value):
        self._sales_ten_m = value
    @property
    def sales_three_m(self):
        return self._sales_three_m

    @sales_three_m.setter
    def sales_three_m(self, value):
        self._sales_three_m = value
    @property
    def sales_three_q(self):
        return self._sales_three_q

    @sales_three_q.setter
    def sales_three_q(self, value):
        self._sales_three_q = value
    @property
    def sales_three_w(self):
        return self._sales_three_w

    @sales_three_w.setter
    def sales_three_w(self, value):
        self._sales_three_w = value
    @property
    def sales_twelve_m(self):
        return self._sales_twelve_m

    @sales_twelve_m.setter
    def sales_twelve_m(self, value):
        self._sales_twelve_m = value
    @property
    def sales_two_m(self):
        return self._sales_two_m

    @sales_two_m.setter
    def sales_two_m(self, value):
        self._sales_two_m = value
    @property
    def sales_two_q(self):
        return self._sales_two_q

    @sales_two_q.setter
    def sales_two_q(self, value):
        self._sales_two_q = value
    @property
    def sales_two_w(self):
        return self._sales_two_w

    @sales_two_w.setter
    def sales_two_w(self, value):
        self._sales_two_w = value
    @property
    def sales_two_y(self):
        return self._sales_two_y

    @sales_two_y.setter
    def sales_two_y(self, value):
        self._sales_two_y = value
    @property
    def seller_status(self):
        return self._seller_status

    @seller_status.setter
    def seller_status(self, value):
        self._seller_status = value
    @property
    def t_thirteen_wk_fba(self):
        return self._t_thirteen_wk_fba

    @t_thirteen_wk_fba.setter
    def t_thirteen_wk_fba(self, value):
        self._t_thirteen_wk_fba = value
    @property
    def t_three_m_fba_inv_value(self):
        return self._t_three_m_fba_inv_value

    @t_three_m_fba_inv_value.setter
    def t_three_m_fba_inv_value(self, value):
        self._t_three_m_fba_inv_value = value
    @property
    def tenure(self):
        return self._tenure

    @tenure.setter
    def tenure(self, value):
        self._tenure = value
    @property
    def ttm_cancellations(self):
        return self._ttm_cancellations

    @ttm_cancellations.setter
    def ttm_cancellations(self, value):
        self._ttm_cancellations = value
    @property
    def ttm_enforcements(self):
        return self._ttm_enforcements

    @ttm_enforcements.setter
    def ttm_enforcements(self, value):
        self._ttm_enforcements = value
    @property
    def ttm_feedback(self):
        return self._ttm_feedback

    @ttm_feedback.setter
    def ttm_feedback(self, value):
        self._ttm_feedback = value
    @property
    def ttm_late_shipments(self):
        return self._ttm_late_shipments

    @ttm_late_shipments.setter
    def ttm_late_shipments(self, value):
        self._ttm_late_shipments = value
    @property
    def ttm_neg_feedback(self):
        return self._ttm_neg_feedback

    @ttm_neg_feedback.setter
    def ttm_neg_feedback(self, value):
        self._ttm_neg_feedback = value
    @property
    def ttm_order_defects(self):
        return self._ttm_order_defects

    @ttm_order_defects.setter
    def ttm_order_defects(self, value):
        self._ttm_order_defects = value
    @property
    def ttm_orders(self):
        return self._ttm_orders

    @ttm_orders.setter
    def ttm_orders(self, value):
        self._ttm_orders = value
    @property
    def ttm_returns(self):
        return self._ttm_returns

    @ttm_returns.setter
    def ttm_returns(self, value):
        self._ttm_returns = value


    def to_alipay_dict(self):
        params = dict()
        if self.curr_fba_inv_value:
            if hasattr(self.curr_fba_inv_value, 'to_alipay_dict'):
                params['curr_fba_inv_value'] = self.curr_fba_inv_value.to_alipay_dict()
            else:
                params['curr_fba_inv_value'] = self.curr_fba_inv_value
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.disbursements_eight_m:
            if hasattr(self.disbursements_eight_m, 'to_alipay_dict'):
                params['disbursements_eight_m'] = self.disbursements_eight_m.to_alipay_dict()
            else:
                params['disbursements_eight_m'] = self.disbursements_eight_m
        if self.disbursements_eight_q:
            if hasattr(self.disbursements_eight_q, 'to_alipay_dict'):
                params['disbursements_eight_q'] = self.disbursements_eight_q.to_alipay_dict()
            else:
                params['disbursements_eight_q'] = self.disbursements_eight_q
        if self.disbursements_eleven_m:
            if hasattr(self.disbursements_eleven_m, 'to_alipay_dict'):
                params['disbursements_eleven_m'] = self.disbursements_eleven_m.to_alipay_dict()
            else:
                params['disbursements_eleven_m'] = self.disbursements_eleven_m
        if self.disbursements_five_m:
            if hasattr(self.disbursements_five_m, 'to_alipay_dict'):
                params['disbursements_five_m'] = self.disbursements_five_m.to_alipay_dict()
            else:
                params['disbursements_five_m'] = self.disbursements_five_m
        if self.disbursements_five_q:
            if hasattr(self.disbursements_five_q, 'to_alipay_dict'):
                params['disbursements_five_q'] = self.disbursements_five_q.to_alipay_dict()
            else:
                params['disbursements_five_q'] = self.disbursements_five_q
        if self.disbursements_five_w:
            if hasattr(self.disbursements_five_w, 'to_alipay_dict'):
                params['disbursements_five_w'] = self.disbursements_five_w.to_alipay_dict()
            else:
                params['disbursements_five_w'] = self.disbursements_five_w
        if self.disbursements_four_m:
            if hasattr(self.disbursements_four_m, 'to_alipay_dict'):
                params['disbursements_four_m'] = self.disbursements_four_m.to_alipay_dict()
            else:
                params['disbursements_four_m'] = self.disbursements_four_m
        if self.disbursements_four_q:
            if hasattr(self.disbursements_four_q, 'to_alipay_dict'):
                params['disbursements_four_q'] = self.disbursements_four_q.to_alipay_dict()
            else:
                params['disbursements_four_q'] = self.disbursements_four_q
        if self.disbursements_four_w:
            if hasattr(self.disbursements_four_w, 'to_alipay_dict'):
                params['disbursements_four_w'] = self.disbursements_four_w.to_alipay_dict()
            else:
                params['disbursements_four_w'] = self.disbursements_four_w
        if self.disbursements_nine_m:
            if hasattr(self.disbursements_nine_m, 'to_alipay_dict'):
                params['disbursements_nine_m'] = self.disbursements_nine_m.to_alipay_dict()
            else:
                params['disbursements_nine_m'] = self.disbursements_nine_m
        if self.disbursements_one_m:
            if hasattr(self.disbursements_one_m, 'to_alipay_dict'):
                params['disbursements_one_m'] = self.disbursements_one_m.to_alipay_dict()
            else:
                params['disbursements_one_m'] = self.disbursements_one_m
        if self.disbursements_one_q:
            if hasattr(self.disbursements_one_q, 'to_alipay_dict'):
                params['disbursements_one_q'] = self.disbursements_one_q.to_alipay_dict()
            else:
                params['disbursements_one_q'] = self.disbursements_one_q
        if self.disbursements_one_w:
            if hasattr(self.disbursements_one_w, 'to_alipay_dict'):
                params['disbursements_one_w'] = self.disbursements_one_w.to_alipay_dict()
            else:
                params['disbursements_one_w'] = self.disbursements_one_w
        if self.disbursements_one_y:
            if hasattr(self.disbursements_one_y, 'to_alipay_dict'):
                params['disbursements_one_y'] = self.disbursements_one_y.to_alipay_dict()
            else:
                params['disbursements_one_y'] = self.disbursements_one_y
        if self.disbursements_seven_m:
            if hasattr(self.disbursements_seven_m, 'to_alipay_dict'):
                params['disbursements_seven_m'] = self.disbursements_seven_m.to_alipay_dict()
            else:
                params['disbursements_seven_m'] = self.disbursements_seven_m
        if self.disbursements_seven_q:
            if hasattr(self.disbursements_seven_q, 'to_alipay_dict'):
                params['disbursements_seven_q'] = self.disbursements_seven_q.to_alipay_dict()
            else:
                params['disbursements_seven_q'] = self.disbursements_seven_q
        if self.disbursements_six_m:
            if hasattr(self.disbursements_six_m, 'to_alipay_dict'):
                params['disbursements_six_m'] = self.disbursements_six_m.to_alipay_dict()
            else:
                params['disbursements_six_m'] = self.disbursements_six_m
        if self.disbursements_six_q:
            if hasattr(self.disbursements_six_q, 'to_alipay_dict'):
                params['disbursements_six_q'] = self.disbursements_six_q.to_alipay_dict()
            else:
                params['disbursements_six_q'] = self.disbursements_six_q
        if self.disbursements_six_w:
            if hasattr(self.disbursements_six_w, 'to_alipay_dict'):
                params['disbursements_six_w'] = self.disbursements_six_w.to_alipay_dict()
            else:
                params['disbursements_six_w'] = self.disbursements_six_w
        if self.disbursements_ten_m:
            if hasattr(self.disbursements_ten_m, 'to_alipay_dict'):
                params['disbursements_ten_m'] = self.disbursements_ten_m.to_alipay_dict()
            else:
                params['disbursements_ten_m'] = self.disbursements_ten_m
        if self.disbursements_three_m:
            if hasattr(self.disbursements_three_m, 'to_alipay_dict'):
                params['disbursements_three_m'] = self.disbursements_three_m.to_alipay_dict()
            else:
                params['disbursements_three_m'] = self.disbursements_three_m
        if self.disbursements_three_q:
            if hasattr(self.disbursements_three_q, 'to_alipay_dict'):
                params['disbursements_three_q'] = self.disbursements_three_q.to_alipay_dict()
            else:
                params['disbursements_three_q'] = self.disbursements_three_q
        if self.disbursements_three_w:
            if hasattr(self.disbursements_three_w, 'to_alipay_dict'):
                params['disbursements_three_w'] = self.disbursements_three_w.to_alipay_dict()
            else:
                params['disbursements_three_w'] = self.disbursements_three_w
        if self.disbursements_twelve_m:
            if hasattr(self.disbursements_twelve_m, 'to_alipay_dict'):
                params['disbursements_twelve_m'] = self.disbursements_twelve_m.to_alipay_dict()
            else:
                params['disbursements_twelve_m'] = self.disbursements_twelve_m
        if self.disbursements_two_m:
            if hasattr(self.disbursements_two_m, 'to_alipay_dict'):
                params['disbursements_two_m'] = self.disbursements_two_m.to_alipay_dict()
            else:
                params['disbursements_two_m'] = self.disbursements_two_m
        if self.disbursements_two_q:
            if hasattr(self.disbursements_two_q, 'to_alipay_dict'):
                params['disbursements_two_q'] = self.disbursements_two_q.to_alipay_dict()
            else:
                params['disbursements_two_q'] = self.disbursements_two_q
        if self.disbursements_two_w:
            if hasattr(self.disbursements_two_w, 'to_alipay_dict'):
                params['disbursements_two_w'] = self.disbursements_two_w.to_alipay_dict()
            else:
                params['disbursements_two_w'] = self.disbursements_two_w
        if self.disbursements_two_y:
            if hasattr(self.disbursements_two_y, 'to_alipay_dict'):
                params['disbursements_two_y'] = self.disbursements_two_y.to_alipay_dict()
            else:
                params['disbursements_two_y'] = self.disbursements_two_y
        if self.marketplace_country:
            if hasattr(self.marketplace_country, 'to_alipay_dict'):
                params['marketplace_country'] = self.marketplace_country.to_alipay_dict()
            else:
                params['marketplace_country'] = self.marketplace_country
        if self.offer_id:
            if hasattr(self.offer_id, 'to_alipay_dict'):
                params['offer_id'] = self.offer_id.to_alipay_dict()
            else:
                params['offer_id'] = self.offer_id
        if self.primary_category_last_three_month_sales_value:
            if hasattr(self.primary_category_last_three_month_sales_value, 'to_alipay_dict'):
                params['primary_category_last_three_month_sales_value'] = self.primary_category_last_three_month_sales_value.to_alipay_dict()
            else:
                params['primary_category_last_three_month_sales_value'] = self.primary_category_last_three_month_sales_value
        if self.primary_product_category:
            if hasattr(self.primary_product_category, 'to_alipay_dict'):
                params['primary_product_category'] = self.primary_product_category.to_alipay_dict()
            else:
                params['primary_product_category'] = self.primary_product_category
        if self.report_card_data_date:
            if hasattr(self.report_card_data_date, 'to_alipay_dict'):
                params['report_card_data_date'] = self.report_card_data_date.to_alipay_dict()
            else:
                params['report_card_data_date'] = self.report_card_data_date
        if self.sales_eight_m:
            if hasattr(self.sales_eight_m, 'to_alipay_dict'):
                params['sales_eight_m'] = self.sales_eight_m.to_alipay_dict()
            else:
                params['sales_eight_m'] = self.sales_eight_m
        if self.sales_eight_q:
            if hasattr(self.sales_eight_q, 'to_alipay_dict'):
                params['sales_eight_q'] = self.sales_eight_q.to_alipay_dict()
            else:
                params['sales_eight_q'] = self.sales_eight_q
        if self.sales_eleven_m:
            if hasattr(self.sales_eleven_m, 'to_alipay_dict'):
                params['sales_eleven_m'] = self.sales_eleven_m.to_alipay_dict()
            else:
                params['sales_eleven_m'] = self.sales_eleven_m
        if self.sales_five_m:
            if hasattr(self.sales_five_m, 'to_alipay_dict'):
                params['sales_five_m'] = self.sales_five_m.to_alipay_dict()
            else:
                params['sales_five_m'] = self.sales_five_m
        if self.sales_five_q:
            if hasattr(self.sales_five_q, 'to_alipay_dict'):
                params['sales_five_q'] = self.sales_five_q.to_alipay_dict()
            else:
                params['sales_five_q'] = self.sales_five_q
        if self.sales_five_w:
            if hasattr(self.sales_five_w, 'to_alipay_dict'):
                params['sales_five_w'] = self.sales_five_w.to_alipay_dict()
            else:
                params['sales_five_w'] = self.sales_five_w
        if self.sales_four_m:
            if hasattr(self.sales_four_m, 'to_alipay_dict'):
                params['sales_four_m'] = self.sales_four_m.to_alipay_dict()
            else:
                params['sales_four_m'] = self.sales_four_m
        if self.sales_four_q:
            if hasattr(self.sales_four_q, 'to_alipay_dict'):
                params['sales_four_q'] = self.sales_four_q.to_alipay_dict()
            else:
                params['sales_four_q'] = self.sales_four_q
        if self.sales_four_w:
            if hasattr(self.sales_four_w, 'to_alipay_dict'):
                params['sales_four_w'] = self.sales_four_w.to_alipay_dict()
            else:
                params['sales_four_w'] = self.sales_four_w
        if self.sales_nine_m:
            if hasattr(self.sales_nine_m, 'to_alipay_dict'):
                params['sales_nine_m'] = self.sales_nine_m.to_alipay_dict()
            else:
                params['sales_nine_m'] = self.sales_nine_m
        if self.sales_one_m:
            if hasattr(self.sales_one_m, 'to_alipay_dict'):
                params['sales_one_m'] = self.sales_one_m.to_alipay_dict()
            else:
                params['sales_one_m'] = self.sales_one_m
        if self.sales_one_q:
            if hasattr(self.sales_one_q, 'to_alipay_dict'):
                params['sales_one_q'] = self.sales_one_q.to_alipay_dict()
            else:
                params['sales_one_q'] = self.sales_one_q
        if self.sales_one_w:
            if hasattr(self.sales_one_w, 'to_alipay_dict'):
                params['sales_one_w'] = self.sales_one_w.to_alipay_dict()
            else:
                params['sales_one_w'] = self.sales_one_w
        if self.sales_one_y:
            if hasattr(self.sales_one_y, 'to_alipay_dict'):
                params['sales_one_y'] = self.sales_one_y.to_alipay_dict()
            else:
                params['sales_one_y'] = self.sales_one_y
        if self.sales_seven_m:
            if hasattr(self.sales_seven_m, 'to_alipay_dict'):
                params['sales_seven_m'] = self.sales_seven_m.to_alipay_dict()
            else:
                params['sales_seven_m'] = self.sales_seven_m
        if self.sales_seven_q:
            if hasattr(self.sales_seven_q, 'to_alipay_dict'):
                params['sales_seven_q'] = self.sales_seven_q.to_alipay_dict()
            else:
                params['sales_seven_q'] = self.sales_seven_q
        if self.sales_six_m:
            if hasattr(self.sales_six_m, 'to_alipay_dict'):
                params['sales_six_m'] = self.sales_six_m.to_alipay_dict()
            else:
                params['sales_six_m'] = self.sales_six_m
        if self.sales_six_q:
            if hasattr(self.sales_six_q, 'to_alipay_dict'):
                params['sales_six_q'] = self.sales_six_q.to_alipay_dict()
            else:
                params['sales_six_q'] = self.sales_six_q
        if self.sales_six_w:
            if hasattr(self.sales_six_w, 'to_alipay_dict'):
                params['sales_six_w'] = self.sales_six_w.to_alipay_dict()
            else:
                params['sales_six_w'] = self.sales_six_w
        if self.sales_stability_score:
            if hasattr(self.sales_stability_score, 'to_alipay_dict'):
                params['sales_stability_score'] = self.sales_stability_score.to_alipay_dict()
            else:
                params['sales_stability_score'] = self.sales_stability_score
        if self.sales_ten_m:
            if hasattr(self.sales_ten_m, 'to_alipay_dict'):
                params['sales_ten_m'] = self.sales_ten_m.to_alipay_dict()
            else:
                params['sales_ten_m'] = self.sales_ten_m
        if self.sales_three_m:
            if hasattr(self.sales_three_m, 'to_alipay_dict'):
                params['sales_three_m'] = self.sales_three_m.to_alipay_dict()
            else:
                params['sales_three_m'] = self.sales_three_m
        if self.sales_three_q:
            if hasattr(self.sales_three_q, 'to_alipay_dict'):
                params['sales_three_q'] = self.sales_three_q.to_alipay_dict()
            else:
                params['sales_three_q'] = self.sales_three_q
        if self.sales_three_w:
            if hasattr(self.sales_three_w, 'to_alipay_dict'):
                params['sales_three_w'] = self.sales_three_w.to_alipay_dict()
            else:
                params['sales_three_w'] = self.sales_three_w
        if self.sales_twelve_m:
            if hasattr(self.sales_twelve_m, 'to_alipay_dict'):
                params['sales_twelve_m'] = self.sales_twelve_m.to_alipay_dict()
            else:
                params['sales_twelve_m'] = self.sales_twelve_m
        if self.sales_two_m:
            if hasattr(self.sales_two_m, 'to_alipay_dict'):
                params['sales_two_m'] = self.sales_two_m.to_alipay_dict()
            else:
                params['sales_two_m'] = self.sales_two_m
        if self.sales_two_q:
            if hasattr(self.sales_two_q, 'to_alipay_dict'):
                params['sales_two_q'] = self.sales_two_q.to_alipay_dict()
            else:
                params['sales_two_q'] = self.sales_two_q
        if self.sales_two_w:
            if hasattr(self.sales_two_w, 'to_alipay_dict'):
                params['sales_two_w'] = self.sales_two_w.to_alipay_dict()
            else:
                params['sales_two_w'] = self.sales_two_w
        if self.sales_two_y:
            if hasattr(self.sales_two_y, 'to_alipay_dict'):
                params['sales_two_y'] = self.sales_two_y.to_alipay_dict()
            else:
                params['sales_two_y'] = self.sales_two_y
        if self.seller_status:
            if hasattr(self.seller_status, 'to_alipay_dict'):
                params['seller_status'] = self.seller_status.to_alipay_dict()
            else:
                params['seller_status'] = self.seller_status
        if self.t_thirteen_wk_fba:
            if hasattr(self.t_thirteen_wk_fba, 'to_alipay_dict'):
                params['t_thirteen_wk_fba'] = self.t_thirteen_wk_fba.to_alipay_dict()
            else:
                params['t_thirteen_wk_fba'] = self.t_thirteen_wk_fba
        if self.t_three_m_fba_inv_value:
            if hasattr(self.t_three_m_fba_inv_value, 'to_alipay_dict'):
                params['t_three_m_fba_inv_value'] = self.t_three_m_fba_inv_value.to_alipay_dict()
            else:
                params['t_three_m_fba_inv_value'] = self.t_three_m_fba_inv_value
        if self.tenure:
            if hasattr(self.tenure, 'to_alipay_dict'):
                params['tenure'] = self.tenure.to_alipay_dict()
            else:
                params['tenure'] = self.tenure
        if self.ttm_cancellations:
            if hasattr(self.ttm_cancellations, 'to_alipay_dict'):
                params['ttm_cancellations'] = self.ttm_cancellations.to_alipay_dict()
            else:
                params['ttm_cancellations'] = self.ttm_cancellations
        if self.ttm_enforcements:
            if hasattr(self.ttm_enforcements, 'to_alipay_dict'):
                params['ttm_enforcements'] = self.ttm_enforcements.to_alipay_dict()
            else:
                params['ttm_enforcements'] = self.ttm_enforcements
        if self.ttm_feedback:
            if hasattr(self.ttm_feedback, 'to_alipay_dict'):
                params['ttm_feedback'] = self.ttm_feedback.to_alipay_dict()
            else:
                params['ttm_feedback'] = self.ttm_feedback
        if self.ttm_late_shipments:
            if hasattr(self.ttm_late_shipments, 'to_alipay_dict'):
                params['ttm_late_shipments'] = self.ttm_late_shipments.to_alipay_dict()
            else:
                params['ttm_late_shipments'] = self.ttm_late_shipments
        if self.ttm_neg_feedback:
            if hasattr(self.ttm_neg_feedback, 'to_alipay_dict'):
                params['ttm_neg_feedback'] = self.ttm_neg_feedback.to_alipay_dict()
            else:
                params['ttm_neg_feedback'] = self.ttm_neg_feedback
        if self.ttm_order_defects:
            if hasattr(self.ttm_order_defects, 'to_alipay_dict'):
                params['ttm_order_defects'] = self.ttm_order_defects.to_alipay_dict()
            else:
                params['ttm_order_defects'] = self.ttm_order_defects
        if self.ttm_orders:
            if hasattr(self.ttm_orders, 'to_alipay_dict'):
                params['ttm_orders'] = self.ttm_orders.to_alipay_dict()
            else:
                params['ttm_orders'] = self.ttm_orders
        if self.ttm_returns:
            if hasattr(self.ttm_returns, 'to_alipay_dict'):
                params['ttm_returns'] = self.ttm_returns.to_alipay_dict()
            else:
                params['ttm_returns'] = self.ttm_returns
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LendingDataList()
        if 'curr_fba_inv_value' in d:
            o.curr_fba_inv_value = d['curr_fba_inv_value']
        if 'currency' in d:
            o.currency = d['currency']
        if 'disbursements_eight_m' in d:
            o.disbursements_eight_m = d['disbursements_eight_m']
        if 'disbursements_eight_q' in d:
            o.disbursements_eight_q = d['disbursements_eight_q']
        if 'disbursements_eleven_m' in d:
            o.disbursements_eleven_m = d['disbursements_eleven_m']
        if 'disbursements_five_m' in d:
            o.disbursements_five_m = d['disbursements_five_m']
        if 'disbursements_five_q' in d:
            o.disbursements_five_q = d['disbursements_five_q']
        if 'disbursements_five_w' in d:
            o.disbursements_five_w = d['disbursements_five_w']
        if 'disbursements_four_m' in d:
            o.disbursements_four_m = d['disbursements_four_m']
        if 'disbursements_four_q' in d:
            o.disbursements_four_q = d['disbursements_four_q']
        if 'disbursements_four_w' in d:
            o.disbursements_four_w = d['disbursements_four_w']
        if 'disbursements_nine_m' in d:
            o.disbursements_nine_m = d['disbursements_nine_m']
        if 'disbursements_one_m' in d:
            o.disbursements_one_m = d['disbursements_one_m']
        if 'disbursements_one_q' in d:
            o.disbursements_one_q = d['disbursements_one_q']
        if 'disbursements_one_w' in d:
            o.disbursements_one_w = d['disbursements_one_w']
        if 'disbursements_one_y' in d:
            o.disbursements_one_y = d['disbursements_one_y']
        if 'disbursements_seven_m' in d:
            o.disbursements_seven_m = d['disbursements_seven_m']
        if 'disbursements_seven_q' in d:
            o.disbursements_seven_q = d['disbursements_seven_q']
        if 'disbursements_six_m' in d:
            o.disbursements_six_m = d['disbursements_six_m']
        if 'disbursements_six_q' in d:
            o.disbursements_six_q = d['disbursements_six_q']
        if 'disbursements_six_w' in d:
            o.disbursements_six_w = d['disbursements_six_w']
        if 'disbursements_ten_m' in d:
            o.disbursements_ten_m = d['disbursements_ten_m']
        if 'disbursements_three_m' in d:
            o.disbursements_three_m = d['disbursements_three_m']
        if 'disbursements_three_q' in d:
            o.disbursements_three_q = d['disbursements_three_q']
        if 'disbursements_three_w' in d:
            o.disbursements_three_w = d['disbursements_three_w']
        if 'disbursements_twelve_m' in d:
            o.disbursements_twelve_m = d['disbursements_twelve_m']
        if 'disbursements_two_m' in d:
            o.disbursements_two_m = d['disbursements_two_m']
        if 'disbursements_two_q' in d:
            o.disbursements_two_q = d['disbursements_two_q']
        if 'disbursements_two_w' in d:
            o.disbursements_two_w = d['disbursements_two_w']
        if 'disbursements_two_y' in d:
            o.disbursements_two_y = d['disbursements_two_y']
        if 'marketplace_country' in d:
            o.marketplace_country = d['marketplace_country']
        if 'offer_id' in d:
            o.offer_id = d['offer_id']
        if 'primary_category_last_three_month_sales_value' in d:
            o.primary_category_last_three_month_sales_value = d['primary_category_last_three_month_sales_value']
        if 'primary_product_category' in d:
            o.primary_product_category = d['primary_product_category']
        if 'report_card_data_date' in d:
            o.report_card_data_date = d['report_card_data_date']
        if 'sales_eight_m' in d:
            o.sales_eight_m = d['sales_eight_m']
        if 'sales_eight_q' in d:
            o.sales_eight_q = d['sales_eight_q']
        if 'sales_eleven_m' in d:
            o.sales_eleven_m = d['sales_eleven_m']
        if 'sales_five_m' in d:
            o.sales_five_m = d['sales_five_m']
        if 'sales_five_q' in d:
            o.sales_five_q = d['sales_five_q']
        if 'sales_five_w' in d:
            o.sales_five_w = d['sales_five_w']
        if 'sales_four_m' in d:
            o.sales_four_m = d['sales_four_m']
        if 'sales_four_q' in d:
            o.sales_four_q = d['sales_four_q']
        if 'sales_four_w' in d:
            o.sales_four_w = d['sales_four_w']
        if 'sales_nine_m' in d:
            o.sales_nine_m = d['sales_nine_m']
        if 'sales_one_m' in d:
            o.sales_one_m = d['sales_one_m']
        if 'sales_one_q' in d:
            o.sales_one_q = d['sales_one_q']
        if 'sales_one_w' in d:
            o.sales_one_w = d['sales_one_w']
        if 'sales_one_y' in d:
            o.sales_one_y = d['sales_one_y']
        if 'sales_seven_m' in d:
            o.sales_seven_m = d['sales_seven_m']
        if 'sales_seven_q' in d:
            o.sales_seven_q = d['sales_seven_q']
        if 'sales_six_m' in d:
            o.sales_six_m = d['sales_six_m']
        if 'sales_six_q' in d:
            o.sales_six_q = d['sales_six_q']
        if 'sales_six_w' in d:
            o.sales_six_w = d['sales_six_w']
        if 'sales_stability_score' in d:
            o.sales_stability_score = d['sales_stability_score']
        if 'sales_ten_m' in d:
            o.sales_ten_m = d['sales_ten_m']
        if 'sales_three_m' in d:
            o.sales_three_m = d['sales_three_m']
        if 'sales_three_q' in d:
            o.sales_three_q = d['sales_three_q']
        if 'sales_three_w' in d:
            o.sales_three_w = d['sales_three_w']
        if 'sales_twelve_m' in d:
            o.sales_twelve_m = d['sales_twelve_m']
        if 'sales_two_m' in d:
            o.sales_two_m = d['sales_two_m']
        if 'sales_two_q' in d:
            o.sales_two_q = d['sales_two_q']
        if 'sales_two_w' in d:
            o.sales_two_w = d['sales_two_w']
        if 'sales_two_y' in d:
            o.sales_two_y = d['sales_two_y']
        if 'seller_status' in d:
            o.seller_status = d['seller_status']
        if 't_thirteen_wk_fba' in d:
            o.t_thirteen_wk_fba = d['t_thirteen_wk_fba']
        if 't_three_m_fba_inv_value' in d:
            o.t_three_m_fba_inv_value = d['t_three_m_fba_inv_value']
        if 'tenure' in d:
            o.tenure = d['tenure']
        if 'ttm_cancellations' in d:
            o.ttm_cancellations = d['ttm_cancellations']
        if 'ttm_enforcements' in d:
            o.ttm_enforcements = d['ttm_enforcements']
        if 'ttm_feedback' in d:
            o.ttm_feedback = d['ttm_feedback']
        if 'ttm_late_shipments' in d:
            o.ttm_late_shipments = d['ttm_late_shipments']
        if 'ttm_neg_feedback' in d:
            o.ttm_neg_feedback = d['ttm_neg_feedback']
        if 'ttm_order_defects' in d:
            o.ttm_order_defects = d['ttm_order_defects']
        if 'ttm_orders' in d:
            o.ttm_orders = d['ttm_orders']
        if 'ttm_returns' in d:
            o.ttm_returns = d['ttm_returns']
        return o


