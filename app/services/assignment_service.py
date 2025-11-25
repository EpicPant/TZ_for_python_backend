import random
from typing import List, Tuple, Optional
from app.models.operator import Operator


class AssignmentService:
    @staticmethod
    def select_operator_weighted(
        candidates: List[Tuple[Operator, int]],
    ) -> Optional[Operator]:
        if not candidates:
            return None
        total = sum(weight for _, weight in candidates)
        if total == 0:
            return random.choice([op for op, _ in candidates])
        rand = random.uniform(0, total)
        cumulative = 0
        for op, weight in candidates:
            cumulative += weight
            if rand <= cumulative:
                return op
        return candidates[-1][0]
