class StageStatusConstants:
    ExpressEval = {267, 268, 269, 270, 2459}
    EntryExp = {271, 458325, 458326}
    ComplexExp = {272, 273, 274, 458327}
    ExpCouncil = {275, 276, 277, 278, 458328}
    LoanIssue = {279, 20761, 192134, 192135}

class TerminationStatusConstants:
    TerminatedStatus = 391056
    PausedStatus = 458323
    TerminationStatuses = {TerminatedStatus, PausedStatus}

class ColorStatusConstants:
    Refinement = {458326, 274, 276, 269}
    OnApproval = {458325, 279, 273, 458327, 275, 268, 2459}
    Denied = {192134, 277, 270}
    DocProcessing = {271, 272, 192135, 278, 458328}
    LoanReceived = {20761}

class StagePassedConstants:
    ExpressEvalPassed = {271, 458325, 458327, 458326, 273, 458328,
                         275, 276, 277, 278, 279, 192135, 192134, 20761, 3126345, 7552031}
    EntryExpPassed = {273, 458328, 275, 276,
                      277, 278, 279, 192135, 192134, 20761}
    ComplexExpPassed = {458328, 275, 276, 277, 278, 279, 192135, 192134, 20761}
    ExpCouncilPassed = {278, 279, 192135, 192134, 20761}
    LoanIssuePassed = {20761}

